from enum import Enum

class PieceType(Enum):
    X = 1
    O = 2
    
class PlayingPiece:
    def __init__(self, peice):
        self.piece_type = PieceType(peice)
    
    def get_name(self):
        return self.piece_type.name
    
    def get_value(self):
        return self.piece_type.value

class PlayingPeiceX(PlayingPiece):
    def __init__(self):
        super().__init__(1)
        
class PlayingPeiceO(PlayingPiece):
    def __init__(self):
        super().__init__(2)
        
#Board size
# - 2d array board
# - size 3 * 3
# - addPiece(x,y)
# - check for win()

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [["-" for i in range(size)] for i in range(size)]
        self.moves_count = 0
        
    def addPeice(self, row, col, playPeice):
        if self.board[row][col] != '-':
            return False
        else:
            self.board[row][col] = playPeice
            self.moves_count += 1
            return True
        
    def is_full(self):
        return self.moves_count == 9
    
    def getFreeCells(self):
        freeCells = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == '-':
                    freeCells.append((i,j))
        return freeCells
    
    def has_winner(self):
        #check for winner in row
        for row in range(self.size):
            if self.board[row][0] != '-' and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return True
            
        #check for winner in col
        for col in range(self.size):
            if self.board[0][col] != '-' and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True
        
        if self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        
        if self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return True
        
        return False
    
    def print_board(self):
        for row in range(self.size):
            print(" | ".join(self.board[row]))
        print("-----------------")

#Player
# - name
# - playing peice

class Player:
    def __init__(self, name, peiceType):
        self.name = name
        self.peice_type = peiceType
        
    def get_name(self):
        return self.name
    
    def get_symbol(self):
        return self.peice_type.get_name()
    