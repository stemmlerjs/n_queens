
from board import Board 
from query import BoardQueryHelper
from random import randint

# Create a board of NxN
SIZE = 8
board = Board(SIZE)
helper = BoardQueryHelper(board)

'''
find_random_start_index


'''

def find_random_start_index():
    return [randint(0, SIZE - 1), randint(0, SIZE - 1)]

'''
solve_n_queens


'''

def solve_n_queens():
    # Set random start position
    startPosition = find_random_start_index()
    board.set(startPosition[1], startPosition[0], 'q')

    queens_placed = 0;

    # Iterate over each element
    for row in range(SIZE):
        for col in range(SIZE):
            # Check if safe to place queen
            print ("[State Row]: X -> " + str(row) + ", Y -> " + str(col))
            safe = can_place_queen(row, col)
            print ("====== SAFE TO PLAY? ======== ")
            print ("Pos: " + str(row) + " " + str(col) + ", " + str(safe))

            # Place queen if safe to do so
            if safe:
                board.set(col,row, 'q')
                queens_placed = 1 + queens_placed
    
    solved = is_solved(queens_placed)
    

'''
can_place_queen

If all values return true, then we can place the 
queen at the current position.E
'''

def can_place_queen(row, col):
    l  = helper.check_direction(row, col, -1, 0)
    print ('Left', l)
    r  = helper.check_direction(row, col, 1, 0)
    print ('Right', r)
    u  = helper.check_direction(row, col, 0, -1)
    print ('Up', u)
    d  = helper.check_direction(row, col, 0, 1)
    print ('Down', d)
    lu = helper.check_direction(row, col, -1, -1)
    print ('Left Up', lu)
    ru = helper.check_direction(row, col, 1, -1)
    print ('Right Up', ru)
    ld = helper.check_direction(row, col, -1, 1)
    print ('Left Down', ld)
    rd = helper.check_direction(row, col, 1, 1)
    print ('Right Down', rd)

    if l and r and u and d and lu and ru and rd:
        return True
    else:
        return False

'''
The problem is solved if:
    1) There are n queens on the board
    2) Each queen is non threatening to e/o
'''

def is_solved(queens_placed):
    if (queens_placed == SIZE - 1):
        return True
    else:
        return False


board.print()
print (board.board)
# helper.check_direction()
# Choose starting point
solve_n_queens()
board.print()

