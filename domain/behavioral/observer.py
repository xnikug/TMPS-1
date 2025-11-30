# Compatibility wrapper — re-export from new observers package
from .observers import GameEventManager, Observer, LoggerObserver, AchievementObserver

__all__ = ['GameEventManager', 'Observer', 'LoggerObserver', 'AchievementObserver']
