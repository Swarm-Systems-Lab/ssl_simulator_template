# SSL Simulator Project Template

A [Copier](https://copier.readthedocs.io/) template for research/experiment
projects built on top of the Swarm Systems Lab Simulator (`ssl_simulator`).
Notebook-driven, never published as a package - controllers, robot models,
and visualization tools live in an editable-installed `src/` package.

For *publishable libraries* (like `ssl_simulator` itself), see
[`ssl_py_template`](https://github.com/Swarm-Systems-Lab/ssl_py_template) instead.

## Getting Started

### Prerequisites: uv and just

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
```

(Both installers add themselves to `~/.local/bin` - make sure that's on your `PATH`.)

### Generate a New Project

```bash
uv tool install copier
copier copy gh:Swarm-Systems-Lab/ssl_simulator_template my-new-project
cd my-new-project
just setup
just notebook
```

You'll be prompted for the project name, slug, author, and a short
description. Open `notebooks/template.ipynb` once Jupyter Lab starts - it
demonstrates how to define robots, add controllers, run the simulation, and
visualize the results.

### Updating a generated project

```bash
copier update
```

## Template Development

Working on this template itself (not a generated project):

```bash
just setup      # Install template metatesting dependencies
just test       # Run template metatests (includes executing the example notebook)
just lint       # Lint template code
just security   # Run security scans with semgrep
just typecheck  # Run type checks
just pre-commit # Run pre-commit hooks
just generate   # Generate a test project for manual inspection
```

See [docs/template-development.md](docs/template-development.md) for the
full command reference, architecture notes, and contributing guidelines.

## License

MIT
