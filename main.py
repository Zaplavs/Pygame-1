
from main_player import MainPlayer
from bandit import Bandit
from heart import Heart
from game import Game

heart = Heart()
bandit = Bandit()
player = MainPlayer()

game = Game(heart,bandit,player)
game.incilizato()
game.play()
