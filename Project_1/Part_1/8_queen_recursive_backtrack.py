#import Tkinter
from termcolor import colored
import sys
#====== Algorithm =============================================================

def recursive_backtracking(column):
    global temp_solution
    if column == len(init_board):
        return True
    else:
        for row in range(len(init_board)):
            prev_solution = temp_solution
            if legal_move(row, column):
                init_board[row][column] = 'Q'
                temp_solution += "%d " % (row+1)
                print_step(True)
                if recursive_backtracking(column + 1):
                    return True
                init_board[row][column] = '.'
            temp_solution += "%d " % (row+1)
            print_step(False)
            temp_solution = prev_solution
        return False

def legal_move(row, column):
    for col in range(1, column+1):
        if row-col >= 0 and init_board[row-col][column-col] == 'Q':
            return False
        if init_board[row][column-col] == 'Q':
            return False
        if row+col < len(init_board) and init_board[row+col][column-col] == 'Q':
            return False
    return True

#==============================================================================

#====== Creation of Board =====================================================

def print_step(legal):
    strip_solution = temp_solution.strip().split(" ")
    #print "strip_solution; ",strip_solution
    for i in range(len(init_board)):
        if i < len(strip_solution)-1:
            print strip_solution[i],
        elif i == len(strip_solution)-1:
            if legal:
                print colored(strip_solution[i], 'green'),
            else:
                print colored(strip_solution[i], 'red'),
        else:
            print '0',
    print ''

def print_board():
    rownumber = len(init_board)
    print '  a b c d e f g h'
    for i in range(len(init_board)-1, -1, -1):
        print rownumber,
        for j in range(len(init_board)):
            print init_board[i][j],
        print rownumber
        rownumber -= 1
    print '  a b c d e f g h'

# def user_interaction():
#     print 'Place queens (ex. "2 4 6 0 0 0 0 0")'
#     user_input = raw_input().replace(' ', '')
#     while len(user_input) != 8:
#         print 'Place queens (ex. "2 4 6 0 0 0 0 0")'
#         user_input = raw_input().replace(' ', '')
#     return user_input

def user_interaction():
    global start_column
    print 'Place queens (ex. "2 4 6 3 1 8 7 5")'
    user_input = raw_input().split(' ')
    try:
        int_list = list(set([int(i) for i in user_input]))
    except:
        int_list = []
    start_column = len(int_list)
    while len(int_list) < dimension:
        int_list.append(0)
    return tuple(int_list)

def create_board(user_input):
    init_board = []
    for i in range(len(user_input)):
        init_board.append(['.','.','.','.','.','.','.','.'])
    for i in range(len(user_input)):
        if user_input[i] != 0:
            init_board[int(user_input[i])-1][i] = 'Q'
    return init_board

#==============================================================================

#====== Flow Controll =========================================================

dimension = 8
start_column = 0
start_row = 0
user_input = user_interaction()
temp_solution = ''
for i in range(len(user_input)):
    if user_input[i] != 0:
        temp_solution += str(user_input[i])+" "
init_board = create_board(user_input)
# for i in range(start_column, -1, -1):
#     if not legal_move(user_input[i]-1, i):
#         print "Illegal input"
#         sys.exit(0)
print "Temp: ", temp_solution
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
