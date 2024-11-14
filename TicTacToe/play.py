from game import Game
from main import Player, PlayingPeiceX, PlayingPeiceO

class TicTacToe:
    def run():
        pt1 = PlayingPeiceX()
        pt2 = PlayingPeiceO()
        p1 = Player("bhavya", pt1)
        p2 = Player("chiransh", pt2)
        g1 = Game(p1,p2)
        g1.play()
    
if __name__ == "__main__":
    t = TicTacToe
    t.run()