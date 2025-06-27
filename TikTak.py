from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        
        name_1 = input("Enter player one name: ").strip()
        symbol_1 = input("Choose your symbol:\nX or O\n ").strip().upper()
        
        name_2 = input("Enter player two name: ").strip()
        if symbol_1 == "X":
            symbol_2 = "O"
        else:
            symbol_2 = "X"
        print(f"Player 1 has select {symbol_1} and Player two has select {symbol_2}")
        
        self.player1 = Player(name_1 , symbol_1)
        self.player2 = Player(name_2 , symbol_2)
        
        self.currentPlayer = self.player1    
            
    def switch_turn(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1
    
    def get_move(self):
        row = int(input("\nEnter the row number (0–2):\n "))
        col = int(input("\nEnter the col number (0–2): \n"))
        if self.board.update(row, col, self.currentPlayer.symbol):   # use current player's symbol
            return True
        else:
            print("\nInvalid move! Cell already taken.\n")
            return False

    def play(self):
        while True:
            self.board.display()

            print(f"{self.currentPlayer.name}'s turn ({self.currentPlayer.symbol})")
            valid_move = False
            while not valid_move:
                try:
                    valid_move = self.get_move()
                except (ValueError, IndexError):
                    print("\nInvalid input. Enter row and column between 0 and 2.\n")

        # Check for winner
            if self.board.check_winner(self.currentPlayer.symbol):
                self.board.display()
                print(f"Congrats {self.currentPlayer.name}, you win!")
                break

        # Check for draw
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

        # Switch turn
            self.switch_turn()

    def announce_winner(self, winner):
        result = self.play()
        if result == "player1":
            print(f"Congrats {self.player1} wins")
        else:
            print(f"Congrats {self.player2} wins")
        
    
if __name__ == "__main__":
    game = Game()
    game.play()



'''
00 | 01 | 02
10 | 11 | 12
20 | 21 | 22
'''


