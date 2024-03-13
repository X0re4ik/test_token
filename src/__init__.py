import os 

import importlib

for pkg in os.listdir("src"):
    if not pkg.endswith(".py") and not pkg.endswith("__") and pkg in ['auth', 'consumption']:
        print(pkg)
        importlib.import_module(f".{pkg}.models", "src")