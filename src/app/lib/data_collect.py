from app.lib.core_mng import CoreMng
from app.lib.dev.error import ErrApp
from app.lib.style_cli import StyleCLI
from app.paperwork.game_choice import GameChoice
from app.paperwork.terminal_bol import TerminalBool
from app.paperwork.types import Nullable


class DataCollect:

    @classmethod
    def choice(cls: type["DataCollect"]) -> GameChoice:
        StyleCLI.tab()

        msg_err: str = (
            "invalid choice, enter 'rock', 'paper', 'scissors' or their first letter"
        )

        while True:
            try:
                ch: str = input(
                    "Enter your choice (rock/paper/scissors or r/p/s, 'exit' to quit'): "
                )

                as_choice: Nullable[GameChoice] = GameChoice.from_input(ch)

                if as_choice is not None:
                    return as_choice

                ErrApp.err_log(msg_err)
            except Exception:
                ErrApp.err_log(msg_err)

    @classmethod
    def play_again(cls: type["DataCollect"]) -> bool:
        while True:
            try:
                ch: str = (
                    input("Do you want to play another round? (yes/no): ")
                    .strip()
                    .lower()
                )

                # ! as title say, type 'exit at any time' should work also here
                # ! so I allow user to just quit even without typing yes or no (or y/n)
                parsed: Nullable[GameChoice] = GameChoice.from_input(ch)
                if parsed is not None:
                    CoreMng.bye_if_bored(parsed)

                as_bool: Nullable[bool] = TerminalBool.from_input(ch)
                if as_bool is not None:
                    return as_bool

                ErrApp.err_log("invalid choice")

            except Exception as err:
                ErrApp.err_log("invalid choice")
