"""Fixtures and helpers for template generation tests."""

import os
import shlex
import shutil
import subprocess
from pathlib import Path

import pytest

TEMPLATE_ROOT = Path(__file__).parent.parent.absolute()


def run_cmd(cmd: str, cwd: Path | None = None, env: dict[str, str] | None = None) -> str:
    """Run a command and return its combined output."""
    base_env = dict(os.environ, UV_PROJECT_ENVIRONMENT="", VIRTUAL_ENV="")
    if env:
        base_env.update(env)
    result = subprocess.run(
        shlex.split(cmd),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=None if cwd is None else str(cwd),
        env=base_env,
    )
    output = result.stdout.decode()
    assert result.returncode == 0, output
    return output


def run_just(target: str, cwd: Path | None = None) -> str:
    """Invoke a Just target from the generated project."""
    return run_cmd(f"just {target}", cwd=cwd)


def copy_project(project_path: Path) -> Path:
    """Generate a project using the same flow as the justfile."""
    run_cmd(f"uv run copier copy --vcs-ref=HEAD --defaults {TEMPLATE_ROOT} {project_path}")
    run_cmd(f"git -C {project_path} init")
    run_cmd("git add .", cwd=project_path)
    run_cmd("git commit -m 'Initial commit'", cwd=project_path)
    return project_path


@pytest.fixture
def project_path(request) -> Path:
    """Create a generated project for a single test."""
    test_root = TEMPLATE_ROOT / ".test_projects"
    test_root.mkdir(parents=True, exist_ok=True)
    project_dir = test_root / request.node.name
    if project_dir.exists():
        shutil.rmtree(project_dir)
    project_dir.mkdir(parents=True)
    yield copy_project(project_dir)
    shutil.rmtree(project_dir, ignore_errors=True)
