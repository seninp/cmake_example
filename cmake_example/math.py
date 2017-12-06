def mul(a, b):
    """Pure Python-only function"""
    return a * b


def add(a, b):
    """Fallback function"""
    return a + b

try:
    from ._math import add as _add
    add = _add
except ImportError:
    pass
