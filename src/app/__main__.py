from app.lib.core_mng import CoreMng
from app.lib.data_collect import DataCollect
from app.lib.style_cli import StyleCLI
from app.paperwork.ctx_game import CtxGame
from app.paperwork.game_choice import GameChoice
from app.paperwork.types import WinnerT


def main(ctx: CtxGame = CtxGame(), with_welcome: bool = True) -> None:

    if with_welcome:
        StyleCLI.intro()

    user_choice: GameChoice = DataCollect.choice()
    CoreMng.bye_if_bored(user_choice)

    cpu_choice: GameChoice = CoreMng.cpu_choice()

    StyleCLI.compare_choices(user_choice, cpu_choice)

    winner: WinnerT = CoreMng.winner_from(user_choice, cpu_choice)
    StyleCLI.the_winner_is(winner)

    ctx.inc_by_winner(winner)
    StyleCLI.score(ctx)

    play_again: bool = DataCollect.play_again()
    if not play_again:
        CoreMng.bye_if_bored(GameChoice.Q)

    main(ctx, False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\t")
        CoreMng.bye_if_bored(GameChoice.Q)
