import os 

import importlib


MODELS = [
    'auth',
    'consumption',
    'purchases',
    'tags',
]

for pkg in os.listdir("src"):
    if not pkg.endswith(".py") and not pkg.endswith("__") and pkg in MODELS:
        print(pkg)
        importlib.import_module(f".{pkg}.models", "src")