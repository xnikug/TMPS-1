"""
Composite Pattern - Treats individual objects and compositions uniformly.
Allows building tree structures of squads with characters.
"""
from .squad_component import SquadComponent
from .character_component import CharacterComponent
from .squad import Squad

__all__ = [
    'SquadComponent',
    'CharacterComponent',
    'Squad'
]
