
class BoardQueryHelper():

    def __init__(self, board):
        self.board = board


    '''
    check_direction
    @param (Number) - cx - current x position
    @param (Number) - cy - current y position
    @param (Number) - add_x - x direction to add
    @param (Number) - add_y - y direction to add
    @return (Boolean) - "Is the current position going to harm
                        any other queens?"
    '''

    def check_direction(self, cx, cy, add_x, add_y):

        print ("[Pos X]: ", cx, "[Pos Y]: ", cy)

        # check if off the board
        if cx > self.board.get_size() - 1  or cy > self.board.get_size() - 1 or cx < 0 or cy < 0:
            return True
        # Check if interfering with a queen
        elif self.board.board[cx][cy] == "q":
            return False
        else:
            return self.check_direction(cx + add_x, cy + add_y, add_x, add_y)

    