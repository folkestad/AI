
from termcolor import colored
import sys

#====== Algorithm =============================================================

def simulated_annealing(init_solution):
    best_neighbor = init_solution

    while stop():
        neighborhood = get_neighbors(best_neighbor)
        best_candidate = None
        for candidate in neighborhood:
            if best_candidate == None:
                best_candidate = candidate
            if fitness(candidte) > fitness(best_candidate):
                best_candidate = candidate
        



def fitness():
    pass

def stop():
    True

def convert_list_to_tuple(candidate):
    list_representation = []
    for col in range(len(candidate)):
        for row in range(len(candidate)):
            if candidate[row][col] == 'Q':
                list_representation.append(row+1)
    return tuple(list_representation)

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
    user_input = raw_input().split(' ')
    int_list = []
    for i in user_input:
        int_list.append(int(i))
    return tuple(int_list)

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
    preprocessing = tuple(preprocessing)
    return preprocessing

max_number_of_visits = 4
max_iterations = 10000
counter = 0
solutions = []
solution_set = set()
user_input = user_interaction()
start = time.time()
init_board = create_board(preprocessing(user_input))
print_board(init_board)
simulated_annealing(init_board)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start
