from vicodin.core import build_prompt, diagnose, parse_exception
import sys

from typing import Type, Optional
from types import TracebackType


def excepthook(exc_type: Type[BaseException], exc_value: BaseException, exc_traceback: Optional[TracebackType]):
    parsed_exc = parse_exception(exc_type, exc_value, exc_traceback)
    prompt = build_prompt(parsed_exc)
    diagnosis = diagnose(prompt)
    print(diagnosis)


def patch():
    sys.excepthook = excepthook
