"""
Proxy Pattern - Controls access to another object.
Used for lazy-loading character data, logging access, or controlling expensive operations.
"""
from .character_proxy import CharacterProxy

__all__ = ['CharacterProxy']
