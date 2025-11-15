from enum import Enum

from app.lib.dev.error import ErrApp


class GameChoice(Enum):
    ROCK = "r"
    PAPER = "p"
    SCISSORS = "s"
    Q = "exit"

    @classmethod
    def from_input(cls: type["GameChoice"], opt: str) -> "GameChoice | None":
        parsed: str = opt.lower().strip()

        for item in cls:
            if parsed == item.value:
                return item

        return None

    @classmethod
    def as_list(cls: type["GameChoice"]) -> list[str]:
        return [x.value for x in cls]

    def for_printer(self: "GameChoice") -> str:
        match self.value:
            case "r":
                return "rock"
            case "p":
                return "paper"
            case "s":
                return "scissors"
            case _:
                return "👻"
