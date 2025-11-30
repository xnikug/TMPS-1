# Compatibility wrapper — re-export from new commands package
from .commands import Command, HealCommand, AttackCommand, AddToPartyCommand, CommandInvoker

__all__ = ['Command', 'HealCommand', 'AttackCommand', 'AddToPartyCommand', 'CommandInvoker']
