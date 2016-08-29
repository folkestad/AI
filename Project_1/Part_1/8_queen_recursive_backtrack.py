#import Tkinter
#====== Algorithm =============================================================

def recursive_backtracking(column):
    if column == len(chess_board):
        return True
    else:
        for row in range(len(chess_board)):
            if legal_move(row, column):
                chess_board[row][column] = 'Q'
                if recursive_backtracking(column + 1):
                    return True
                chess_board[row][column] = '.'
        return False

def legal_move(row, column):
    for col in range(0, column+1):
        if row-col >= 0 and chess_board[row-col][column-col] == 'Q':
            return False
        if chess_board[row][column-col] == 'Q':
            return False
        if row+col < len(chess_board) and chess_board[row+col][column-col] == 'Q':
            return False
    return True

#==============================================================================

#====== Creation of Board =====================================================

def print_board():
    rownumber = len(chess_board)
    print '  a b c d e f g h'
    for i in range(len(chess_board)-1, -1, -1):
        print rownumber,
        for j in range(len(chess_board)):
            print chess_board[i][j],
        print rownumber
        rownumber -= 1
    print '  a b c d e f g h'

def user_interaction():
    print 'Place queens (ex. "2 4 6 0 0 0 0 0")'
    user_input = raw_input().replace(' ', '')
    while len(user_input) != 8:
        print 'Place queens (ex. "2 4 6 0 0 0 0 0")'
        user_input = raw_input().replace(' ', '')
    return user_input

def create_board(user_input):
    chess_board = []
    for i in range(len(user_input)):
        chess_board.append(['.','.','.','.','.','.','.','.'])
    for i in range(len(user_input)):
        if user_input[i] != '0':
            chess_board[int(user_input[i])-1][i] = 'Q'
    return chess_board

#==============================================================================

#====== Flow Controll =========================================================

user_input = user_interaction()
chess_board = create_board(user_input)
start_column = 0
for i in range(len(user_input)):
    if user_input[i] == '0':
        start_column = i
        break
solution_exists = recursive_backtracking(start_column)
print ""
if solution_exists:
    print_board()
else:
    print "There exists no solution"

#top = Tkinter.Tk()
#Code to add widgets will go here...
#top.mainloop()

#==============================================================================
