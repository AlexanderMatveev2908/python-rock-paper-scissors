import random
from typing import cast
from app.lib.style_cli import StyleCLI
from app.paperwork.game_choice import GameChoice


class CoreMng:

    @classmethod
    def bye_if_bored(cls: type["CoreMng"], ch: GameChoice) -> None:
        if ch == GameChoice.Q:
            StyleCLI.tab()

            print("Bye ✌🏼")
            exit(0)

    @classmethod
    def cpu_choice(cls: type["CoreMng"]) -> GameChoice:

        options: list[str] = GameChoice.as_list()
        choice: str = random.choice(options)

        # ! it can not be null, so casting is not an issue here
        parsed: GameChoice = cast(GameChoice, GameChoice.from_input(choice))

        return parsed
