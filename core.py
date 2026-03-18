"""Core functionality for project5."""

from project4 import mega_greet


def ultra_greet(name: str) -> str:
    """Return an ultra greeting using project4."""
    mega_msg = mega_greet(name)
    return f"{mega_msg} Ultra-enhanced by project5!"
