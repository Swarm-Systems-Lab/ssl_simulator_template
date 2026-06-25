# SSL Simulator Project Template

This repository provides a **ready-to-use template** for creating new research/experiment projects built on top of the Swarm Systems Lab (SSL) Simulator (`ssl_simulator`).
It includes recommended folder structures, example notebooks, controllers, robot models, and visualization tools.

Unlike [`ssl_py_template`](https://github.com/Swarm-Systems-Lab/ssl_py_template) (used for *publishable libraries* like `ssl_simulator` itself), this template is for projects that *consume* `ssl_simulator` - research/experiment repos that are never published as a package, typically notebook-driven, with no CI/publish machinery attached.

You generate a new project using [**Copier**](https://copier.readthedocs.io/).

---

## Getting Started

### 1. Install Copier

```bash
uv tool install copier
# or: pipx install copier
```

### 2. Generate a New Project

```bash
copier copy gh:Swarm-Systems-Lab/ssl_simulator_template my-new-project
```

- You'll be prompted for the project name, slug, author, and a short description.

### 3. Explore Your New Project

```bash
cd my-new-project
uv sync
```

You'll get:

- `src/` with example controllers, robot models, and visualization classes
- `notebooks/` with a starter Jupyter notebook
- `output/` for simulation data (gitignored)
- `pyproject.toml` declaring `ssl_simulator` as a dependency, managed via `uv`

### 4. Run the Example

```bash
just notebook
# or: uv run jupyter lab notebooks/
```

Open `notebooks/template.ipynb` - it demonstrates how to define robots, add
controllers, run the simulation, and visualize the results.

### Updating a generated project

Generated projects can pull in template improvements later via:

```bash
copier update
```

---

## References

- [Copier Documentation](https://copier.readthedocs.io/)
- [SSL Simulator Documentation](https://github.com/Swarm-Systems-Lab/ssl_simulator)
