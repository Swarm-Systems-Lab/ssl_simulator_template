# SSL Simulator Project Template

This repository provides a **ready-to-use template** for creating new projects based on the Swarm Systems Lab (SSL) Simulator.  
It includes recommended folder structures, example notebooks, controllers, robot models, and visualization tools.  

You can quickly generate a new project using **Cookiecutter**.

- All files and folders inside `{{cookiecutter.project_slug}}/` will be copied into your new project.  
- Use the `cookiecutter.json` to customize project name, author, Python version, etc.

---

## - Getting Started -

### 1. Install Cookiecutter

```bash
pip install cookiecutter
```

### 2. Generate a New Project

From any folder, run:

```bash
cookiecutter https://github.com/Swarm-Systems-Lab/ssl_simulator_template.git
```

- You will be prompted to fill in the project name, author, and other variables defined in `cookiecutter.json`.  
- Example:

```
project_name [My Simulation Project]: MyFirstSim
project_slug [my_simulation_project]: my_first_sim
```

---

### 3. Explore Your New Project

```bash
cd my_first_sim
tree
```

You will see the folder structure populated with:

- `src/` containing example controllers, robot models, and visualization classes  
- `notebooks/` with starter Jupyter notebooks  
- `output/` for simulation data  
- `requirements.txt` listing project dependencies

---

### 4. Run a Simulation Example

Open the template notebook:

```bash
jupyter notebook notebooks/template.ipynb
```

- It demonstrates how to define robots, add controllers, run the simulation, and visualize the results.  

---

## References

- [Cookiecutter Documentation](https://cookiecutter.readthedocs.io/en/latest/)  
- [SSL Simulator Documentation](https://github.com/Swarm-Systems-Lab/ssl_simulator)  