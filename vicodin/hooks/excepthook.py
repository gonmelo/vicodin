from vicodin.core import diagnose
import sys


def excepthook(except_type, except_value, except_traceback):
    diagnose(except_value)


def patch():
    sys.excepthook = excepthook
