from game.engine import GameEngine

if __name__ == '__main__':
    game_engine = GameEngine()
    print(type(game_engine))
    print(type(GameEngine))  # type
    # game_engine.current_step = 5  # this is a dynamic attribute which is not used anywhere
    game_engine.run()

    # if game_engine.winner is not None:
    if game_engine.winner:
        # print(type(game_engine.winner))
        print("Game was won by Player:", game_engine.winner)
    else:
        print("Game ended as a draw.")
