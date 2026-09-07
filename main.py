from scripts.Game import Game
from scripts.screens.GameScreen import GameScreen

game = Game()

game.change_current_screen(GameScreen(game))

game.run()