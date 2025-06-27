class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self, show=None):  
        print("Current Board: ")
        for row in self.grid:
            print(" | ".join(row))
            print("--+--+--")

    def is_cell_empty(self, row, col):
        return self.grid[row][col] == ' ' 

    def update(self, row, col, symbol):
        if self.is_cell_empty(row, col):  
            self.grid[row][col] = symbol
            return True
        else:
            return False

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == ' ':
                    return False
        return True  

    def check_winner(self, symbol):
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True

        if all(self.grid[i][i] == symbol for i in range(3)):
            return True

        if all(self.grid[i][2 - i] == symbol for i in range(3)):
            return True

        return False
