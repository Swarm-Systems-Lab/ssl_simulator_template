# Template Development

Notes for working on `ssl_simulator_template` itself - not relevant if you're
just generating a project from it (see the root [README](../README.md) for that).

## Repository Structure

```
ssl_simulator_template/
├── template/              # Template content (copied into generated projects)
│   ├── src/{{ project_slug }}/   # controllers/, robot_models/, visualization/
│   ├── notebooks/
│   ├── output/             # gitignored, except .gitkeep
│   ├── pyproject.toml.jinja # uv-managed, ssl_simulator dependency
│   └── justfile
├── tests/                  # Metatests that validate the template itself
├── docs/                   # This documentation
├── .github/workflows/      # CI for this repo (tests the template, not a generated project)
├── justfile                # Template dev commands (just test, just lint, ...)
├── pyproject.toml          # Metatesting dependencies
└── copier.yml              # Template configuration (questions asked on generation)
```

## Command Reference

```bash
just setup           # Install dependencies with uv
just sync            # Sync all dependency groups
just build           # Build package in development mode

just lint            # Run ruff formatting and linting
just typecheck       # Run type checking with ty (against tests/)
just pre-commit      # Run pre-commit hooks on all files
just security        # Run security scans with semgrep

just test            # Run all metatests with tox (recommended)
just test-fast       # Run metatests in parallel, skip slow tests
just test-multi-py   # Run metatests across Python 3.12-3.14
just list            # List all tox environments

just publish         # Publish with uv (requires UV_PUBLISH_* env vars)
just publish-ci      # Publish with twine (CI-friendly; requires TWINE_* env vars)

just generate        # Generate a test project for manual inspection
just act             # Test this repo's own GitHub Actions workflows locally

just clean           # Clean build and test artifacts
```

## Metatests

`just test` runs `tests/test_template.py`, which generates a project with
`copier copy --defaults` and checks:

- The expected files exist in the generated output
- The generated project has a usable git repository
- `just setup` succeeds and the generated package is importable
- **The example notebook executes end-to-end with zero errors** (via
  `nbconvert`), and produces real simulation output

Test projects are created under `.test_projects/` (gitignored), and removed
after each run.

## Architecture Notes

**Why a separate template from `ssl_py_template`?** This template generates
*consumers* of `ssl_simulator` - research/experiment repos that are never
published, typically notebook-driven. `ssl_py_template` generates
*publishable libraries* with CI/publish machinery attached. Conflating the
two would force one of them to carry irrelevant complexity.

**Why an editable-installed `src/{{ project_slug }}/` package, not
`sys.path` hacks?** So notebooks import normally
(`from {{ project_slug }}.controllers import X`) with no manual path
manipulation. Combined with `%autoreload 2` in the notebook, edits to `src/`
show up without restarting the kernel.

## Contributing

1. Make changes under `template/`
2. `just test` to validate the template still generates a working project
   (including a full notebook execution)
3. `just generate` to inspect a generated project manually if needed
4. `just lint` before committing
