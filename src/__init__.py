import os 

import importlib


MODELS = [
    'secrets',
    'auth',
    'tags',
]

for pkg in os.listdir("src"):
    if not pkg.endswith(".py") and not pkg.endswith("__") and pkg in MODELS:
        importlib.import_module(f".{pkg}.models", "src")