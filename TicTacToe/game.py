from main import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board(3)
        self.current_player = player1

    def play(self):
        self.board.print_board()
        while self.board.is_full() == False and self.board.has_winner() == False:
            print(f"{self.current_player.get_name()}'s turn")
            row = self.get_valid_input("Enter row(0-2): ")
            col = self.get_valid_input("Enter col(0-2): ")
            
            if self.board.addPeice(row, col, self.current_player.get_symbol()):
                self.board.print_board()
                self.switch_player()
            else:
                self.board.print_board()
                print("This place is already taken. Please enter other place")
            
        if self.board.has_winner():
            self.switch_player()
            print(f"{self.current_player.get_name()} wins!")
        else:
            print("Match draw")            
    
    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
            
    def get_valid_input(self, message):
        while True:
            try:
                user_input = int(input(message))
                if 0 <= user_input <= 2:
                    return user_input
                else:
                    print("Invalid input! Please enter a number between 0 and 2")
            except ValueError:
                print("Invalid input! Please enter a number between 0 and 2")