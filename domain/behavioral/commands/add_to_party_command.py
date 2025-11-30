from .command import Command
from domain.singleton.game_manager import GameManager


class AddToPartyCommand(Command):
    def __init__(self, character):
        self.character = character
        self._added = False
        self._gm = GameManager()

    def execute(self) -> None:
        self._added = self._gm.add_to_party(self.character)

    def log(self) -> str:
        if self._added:
            return f"{self.character.name} was added to the party."
        else:
            return f"{self.character.name} could not be added to the party (maybe already present)."
    
    def undo(self) -> None:
        if self._added and self.character in self._gm.current_party:
            self._gm.current_party.remove(self.character)
            self._added = False
