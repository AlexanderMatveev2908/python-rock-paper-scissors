from app.lib.dev.error import ErrApp
from app.paperwork.game_choice import GameChoice
from app.paperwork.types import Nullable


class DataCollect:

    @classmethod
    def choice(cls: type["DataCollect"]) -> GameChoice:
        while True:
            try:
                ch: str = input(
                    "Enter your choice (rock/paper/scissors or r/r/s, 'exit' to quit'): "
                )

                as_choice: Nullable[GameChoice] = GameChoice.from_input(ch)

                if as_choice is not None:
                    return as_choice

                ErrApp.err_log("Invalid choice")
            except Exception as err:
                ErrApp.err_log("Invalid choice")
