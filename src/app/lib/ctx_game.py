from app.paperwork.types import WinnerT


class CtxGame:
    user: int = 0
    cpu: int = 0
    ties: int = 0

    def inc_by_winner(self: "CtxGame", w: WinnerT) -> None:
        match w:
            case "USER":
                self.user += 1
            case "CPU":
                self.cpu += 1
            case "TIE":
                self.ties += 1
