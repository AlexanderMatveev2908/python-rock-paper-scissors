from enum import Enum


class GameChoice(Enum):
    ROCK = "r"
    PAPER = "p"
    SCISSORS = "s"
    Q = "exit"

    @classmethod
    def from_input(cls: type["GameChoice"], opt: str) -> "GameChoice | None":
        if not opt:
            return None

        parsed: str = opt.lower().strip()

        for item in cls:
            if parsed == item.value or (
                parsed[0] == item.value and item.value != "exit"
            ):
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
            case "exit":
                return "👻"
            case _:
                return "👻"

    def emj(self: "GameChoice") -> str:
        match self.value:
            case "r":
                return "✊"
            case "p":
                return "🖐️"
            case "s":
                return "✌️"
            case "exit":
                return "👻"
            case _:
                return "👻"
