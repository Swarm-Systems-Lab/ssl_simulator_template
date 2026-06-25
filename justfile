# justfile for developing this template itself (not for generated projects)

# Setup the template's metatesting environment
setup:
    uv lock
    uv sync --extra dev

# Run template generation metatests
test:
    uv run pytest tests

# Lint template code
lint:
    uv run ruff format tests
    uv run ruff check tests --fix

# Generate a test project locally for manual inspection
generate OUTPUT="./.test_projects/just_project":
    uv run copier copy --vcs-ref=HEAD --defaults . {{OUTPUT}}
    git -C {{OUTPUT}} init
    git -C {{OUTPUT}} add .
    git -C {{OUTPUT}} commit -m "Initial commit"
    @echo "Test project generated at: {{OUTPUT}}"

# Clean build/test artifacts
clean:
    rm -rf .venv .pytest_cache .ruff_cache .test_projects
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
