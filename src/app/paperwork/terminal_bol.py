from enum import Enum

from app.paperwork.types import Nullable


class TerminalBool(Enum):
    YES = "y"
    NO = "n"

    @classmethod
    def from_input(cls: type["TerminalBool"], ch: str) -> Nullable[bool]:
        if not ch:
            return None

        for opt in cls:
            val: str = opt.value

            if ch == val or ch[0] == val:
                return val == "y"

        return None
