from app.paperwork.game_choice import GameChoice
from app.paperwork.types import WinnerT


class StyleCLI:
    @classmethod
    def tab(cls: type["StyleCLI"]) -> None:
        print("\t")

    @classmethod
    def intro(cls: type["StyleCLI"]) -> None:
        print("🕹️ Welcome to Rock-Paper-Scissors CLI!")
        print("Type 'exit' to quit at any time.")

    @classmethod
    def compare_choices(
        cls: type["StyleCLI"], user: GameChoice, cpu: GameChoice
    ) -> None:
        cls.tab()

        print(f"You chose: {user.emj()} {user.for_printer()}")
        print(f"Computer chose: {cpu.emj()} {cpu.for_printer()}")

    @classmethod
    def the_winner_is(cls: type["StyleCLI"], w: WinnerT) -> None:

        match w:
            case "USER":
                print("You win this round 🎉")
            case "CPU":
                print("CPU win this round 🔋")
            case "TIE":
                print("It's a tie 🤝")
