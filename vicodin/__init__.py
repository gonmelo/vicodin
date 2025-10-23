import os
from .hooks.excepthook import patch


if os.getenv("VICODIN_AUTOPATCH", "0") == "1":
    patch()


__all__ = ["patch"]
