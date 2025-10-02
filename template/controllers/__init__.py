import importlib
import pkgutil
import os

# Automatically import all symbols from each module in this package that defines __all__
package_dir = os.path.dirname(__file__)
for _, modname, ispkg in pkgutil.iter_modules([package_dir]):
	if not ispkg and modname != "__init__":
		module = importlib.import_module(f".{modname}", __package__)
		if hasattr(module, "__all__"):
			globals().update({k: getattr(module, k) for k in module.__all__})