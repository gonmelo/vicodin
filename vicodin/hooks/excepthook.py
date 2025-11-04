from vicodin.core import build_prompt, diagnose, parse_traceback
import sys

from typing import Type, Optional
from types import TracebackType


def excepthook(exc_type: Type[BaseException], exc_value: BaseException, exc_traceback: Optional[TracebackType]):
    parsed_tb = parse_traceback(exc_type, exc_value, exc_traceback)
    prompt = build_prompt(parsed_tb)
    diagnosis = diagnose(prompt)


def patch():
    sys.excepthook = excepthook
