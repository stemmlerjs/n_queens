
class Board ():

    '''
     Constructor
    '''
    def __init__(self, size):
        self.board = []
        self.size = size

        # Fill up the board
        for row in range(size):
            self.board.append([])

            # Add column
            for col in range(size):
                self.board[row].append('x')

    '''
    Print the current board
    '''
    def print(self):
        for row in self.board:
            print (" ".join(row))

    '''
    Change a row in the board
    '''
    def set(self, x, y, val):
        self.board[y][x] = val

    def get_size(self):
        return self.size
    
    def reset_board(self):
        # Fill up the board
        for row in range(self.size):
            self.board.append([])

            # Add column
            for col in range(self.size):
                self.board[row].append('x')

        




