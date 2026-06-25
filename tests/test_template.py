"""Focused template generation tests."""

import json
from pathlib import Path

from conftest import run_cmd, run_just


def test_project_files_created(project_path: Path):
    """Generate a default project and verify core files exist."""
    expected_paths = [
        Path("pyproject.toml"),
        Path("README.md"),
        Path("justfile"),
        Path("LICENSE"),
        Path(".copier-answers.yml"),
        Path("notebooks") / "template.ipynb",
        Path("output") / ".gitkeep",
        Path("src") / "my_simulation_project" / "__init__.py",
        Path("src") / "my_simulation_project" / "controllers" / "example_controller.py",
        Path("src") / "my_simulation_project" / "robot_models" / "example_robot.py",
        Path("src") / "my_simulation_project" / "visualization" / "example_plot.py",
    ]

    for rel_path in expected_paths:
        assert (project_path / rel_path).exists(), f"Missing {rel_path}"


def test_git_repo_initialized(project_path: Path):
    """Verify the generated project has a usable git repository."""
    assert (project_path / ".git").is_dir()
    run_cmd("git status -sb", cwd=project_path)


def test_project_can_setup_and_import(project_path: Path):
    """The generated just workflow should lock deps and install an importable package."""
    run_just("setup", project_path)
    assert (project_path / "uv.lock").exists()
    run_cmd(
        "uv run python -c "
        '"from my_simulation_project.controllers import ExampleController; '
        'print(ExampleController)"',
        cwd=project_path,
    )


def test_notebook_executes(project_path: Path):
    """The example notebook should run end-to-end with zero errors."""
    run_just("setup", project_path)
    run_cmd(
        "uv run --with nbconvert jupyter nbconvert --to notebook --execute "
        "--output executed.ipynb notebooks/template.ipynb",
        cwd=project_path,
    )

    executed = json.loads((project_path / "notebooks" / "executed.ipynb").read_text())
    errors = [
        out
        for cell in executed["cells"]
        for out in cell.get("outputs", [])
        if out.get("output_type") == "error"
    ]
    assert not errors, errors
    assert (project_path / "output" / "simulation_data.csv").exists()
