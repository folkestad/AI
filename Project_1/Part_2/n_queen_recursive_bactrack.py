#import Tkinter
from termcolor import colored
#====== Algorithm =============================================================

def recursive_backtracking(column):
    if column == len(chess_board):
        return True
    else:
        for row in range(len(chess_board)):
            if legal_move(row, column):
                chess_board[row][column] = 'Q'
                if recursive_backtracking(column + 1) and column == len(chess_board)-1:
                    solution = ""
                    for i in range(len(chess_board)):
                        for j in range(len(chess_board)):
                            if chess_board[i][j] == 'Q':
                                solution += `i+1`+" "
                    solutions.append(solution)
                chess_board[row][column] = '.'
        return len(solutions) > 0

def recursive_backtracking_step_by_step(column):
    global temp_solution
    global chess_board
    if column == len(chess_board):
        return True
    else:
        for row in range(len(chess_board)):
            prev_solution = temp_solution
            if legal_move(row, column):
                chess_board[row][column] = 'Q'
                temp_solution += "%d " % (row+1)
                print_step(True)
                if recursive_backtracking_step_by_step(column + 1) and column == len(chess_board)-1:
                    solutions.append(temp_solution)
                temp_solution = prev_solution
                chess_board[row][column] = '.'
            else:
                temp_solution += "%d " % (row+1)
                print_step(False)
                temp_solution = prev_solution
        return len(solutions) > 0

def legal_move(row, column):
    for col in range(1, column+1):
        if row-col >= 0 and chess_board[row-col][column-col] == 'Q':
            return False
        if chess_board[row][column-col] == 'Q':
            return False
        if row+col < len(chess_board) and chess_board[row+col][column-col] == 'Q':
            return False
    return True

#==============================================================================

#====== Creation of Board =====================================================

def print_step(legal):
    strip_solution = temp_solution.strip().split(" ")
    for i in range(len(chess_board)):
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
    rownumber = len(chess_board)
    print ' ',
    for i in range(len(chess_board)):
        print chr(97+i),
    print ""

    for i in range(len(chess_board)-1, -1, -1):
        print rownumber,
        for j in range(len(chess_board)):
            print chess_board[i][j],
        print rownumber
        rownumber -= 1

    print ' ',
    for i in range(len(chess_board)):
        print chr(97+i),
    print ""

def print_first_board():
    board = create_board(solutions[0])
    rownumber = len(board)
    print ' ',
    for i in range(len(board)):
        print chr(97+i),
    print ""

    for i in range(len(board)-1, -1, -1):
        print rownumber,
        for j in range(len(board)):
            print board[i][j],
        print rownumber
        rownumber -= 1

    print ' ',
    for i in range(len(board)):
        print chr(97+i),
    print ""

def user_interaction():
    print 'Place queens (ex. "2 4 6 0 0 0 0 0")'
    user_input = raw_input().replace(' ', '')
    return user_input

def create_board(user_input):
    chess_board = []
    for i in range(len(user_input)):
        chess_board.append([])
        for j in range(len(user_input)):
            chess_board[i].append('.')
    for i in range(len(user_input)):
        if user_input[i] != '0':
            chess_board[int(user_input[i])-1][i] = 'Q'
    return chess_board

#==============================================================================

#====== Flow Controll =========================================================

user_input = user_interaction()
print ""
chess_board = create_board(user_input)
start_column = 0
temp_solution = ''
for i in range(len(user_input)):
    if user_input[i] == '0':
        start_column = i
        break
    else:
        temp_solution += user_input[i]+" "
solutions = []
solution_exists = recursive_backtracking_step_by_step(start_column)
print ""
if solution_exists:
    #print_first_board()
    for i in solutions:
        print i
    print ""
    print len(solutions)
else:
    print "There exists no solutions."


#top = Tkinter.Tk()
#Code to add widgets will go here...
#top.mainloop()

#==============================================================================
