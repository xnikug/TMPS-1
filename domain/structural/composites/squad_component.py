"""
Squad Component - Base interface for Composite Pattern
Allows both individual characters and groups of characters to be treated uniformly.
"""
from abc import ABC, abstractmethod
from typing import List


class SquadComponent(ABC):
    """Abstract base component for squad hierarchy."""
    
    @abstractmethod
    def get_total_damage(self) -> int:
        """Calculate total damage the component can deal."""
        pass
    
    @abstractmethod
    def get_total_health(self) -> int:
        """Get total health across component."""
        pass
    
    @abstractmethod
    def get_members_count(self) -> int:
        """Get count of individual characters."""
        pass
    
    @abstractmethod
    def get_average_level(self) -> float:
        """Get average level of squad."""
        pass
    
    @abstractmethod
    def display_info(self, indent: int = 0) -> str:
        """Display hierarchical information."""
        pass
