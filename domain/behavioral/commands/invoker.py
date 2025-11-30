from typing import List
from .command import Command


class CommandInvoker:
    def __init__(self):
        self._history: List[Command] = []

    def execute_command(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def show_command_history(self) -> List[Command]:
        for cmd in self._history:
            print(cmd.log())
    
    def undo_last(self) -> None:
        if not self._history:
            return
        cmd = self._history.pop()
        try:
            cmd.undo()
        except NotImplementedError:
            # ignore commands that don't support undo
            pass
