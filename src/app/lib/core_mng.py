import random
from typing import cast
from app.lib.style_cli import StyleCLI
from app.paperwork.game_choice import GameChoice
from app.paperwork.types import WinnerT


class CoreMng:

    @classmethod
    def bye_if_bored(cls: type["CoreMng"], ch: GameChoice) -> None:
        if ch == GameChoice.Q:
            StyleCLI.tab()

            print("Bye ✌🏼")
            exit(0)

    @classmethod
    def cpu_choice(cls: type["CoreMng"]) -> GameChoice:

        options: list[str] = [x for x in GameChoice.as_list() if x != "exit"]
        choice: str = random.choice(options)

        # ! it can not be null, so casting is not an issue here
        parsed: GameChoice = cast(GameChoice, GameChoice.from_input(choice))

        return parsed

    @classmethod
    def winner_from(cls: type["CoreMng"], user: GameChoice, cpu: GameChoice) -> WinnerT:
        # ! exit never reach this line because I say bye to user if he input exit at any time
        map_wins: dict[GameChoice, GameChoice] = {
            GameChoice.ROCK: GameChoice.SCISSORS,
            GameChoice.PAPER: GameChoice.ROCK,
            GameChoice.SCISSORS: GameChoice.PAPER,
        }

        if map_wins[user] == cpu:
            return "USER"
        elif map_wins[cpu] == user:
            return "CPU"
        else:
            return "TIE"
