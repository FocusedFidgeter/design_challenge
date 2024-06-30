import importlib.util
import os
from typing import Callable
from decimal import Decimal

PaymentHandlerFn = Callable[[Decimal], None]

# Dictionary to hold the payment handlers
PAYMENT_HANDLERS: dict[str, PaymentHandlerFn] = {}

def load_plugins(plugin_folder: str) -> None:
    for file in os.listdir(plugin_folder):
        if file.endswith(".py") and file != "__init__.py":
            module_name = file[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(plugin_folder, file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            PAYMENT_HANDLERS.update(module.get_payment_handlers())