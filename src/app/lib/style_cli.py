from app.paperwork.game_choice import GameChoice


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

        print(f"You chose: {user.for_printer()}")
        print(f"Computer chose: {user.for_printer()}")
