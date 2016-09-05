
from termcolor import colored
import sys

#====== Algorithm =============================================================


#====== Printing of Board =====================================================

def print_board(board):
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

#==============================================================================

#====== Creation of Board =====================================================

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

def user_interaction():
    print 'Place queens (ex. "2 4 6 3 1 8 7 5")'
    user_input = raw_input().replace(' ', '')
    return user_input

def preprocessing(user_input):
    # fixes so that no queen is on the same rownumber
    preprocessing = set()
    for i in range(len(user_input)):
        preprocessing.add(user_input[i])
    if len(user_input) == len(preprocessing):
        return user_input
    for i in range(1, len(user_input)+1):
        if i not in preprocessing:
            character = str(i).encode('utf-8')
            preprocessing.add(character)
    preprocessing = ''.join(list(preprocessing))
    return preprocessing


max_tabu_memory_size = 100
max_number_of_visits = 4
counter = 0
solutions = []
solution_set = set()
user_input = user_interaction()
init_board = create_board(preprocessing(user_input))
print_board(init_board)
tabu_search(init_board)
print ""
print len(solutions)
