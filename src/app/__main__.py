from app.lib.core_mng import CoreMng
from app.lib.data_collect import DataCollect
from app.lib.style_cli import StyleCLI
from app.paperwork.game_choice import GameChoice


def main() -> None:
    StyleCLI.intro()

    user_choice: GameChoice = DataCollect.choice()
    CoreMng.bye_if_bored(user_choice)

    cpu_choice: GameChoice = CoreMng.cpu_choice()

    StyleCLI.compare_choices(user_choice, cpu_choice)


if __name__ == "__main__":
    main()
