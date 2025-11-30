from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass
    @abstractmethod
    def log(self) -> str:
        pass
    def undo(self) -> None:
        raise NotImplementedError("Undo not implemented for this command")
