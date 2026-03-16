"""Core functionality for proj5."""

from proj4 import mega_greet


def ultra_greet(name: str) -> str:
    """Return an ultra greeting using proj4."""
    mega_msg = mega_greet(name)
    return f"{mega_msg} Ultra-enhanced by proj5!"
