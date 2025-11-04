import traceback


def parse_exception(exc_type, exc_value, exc_trace) -> dict:
    tb = traceback.extract_tb(exc_trace)
    frames = []
    for frame in tb:
        frames.append({
            "filename": frame.filename,
            "lineno": frame.lineno,
            "function": frame.name,
            "code": frame.line,
        })
    return {
        "type": exc_type.__name__,
        "message": str(exc_value),
        "frames": frames,
    }
