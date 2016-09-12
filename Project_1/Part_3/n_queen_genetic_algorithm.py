
from termcolor import colored
import sys
import math
import random
import time

#====== Algorithm =============================================================

def genetic_algorithm(init_parent):
    generation_number = 1
    parent = init_parent
    other_parent = random_parent(parent)
    generation = generate_population(parent, other_parent)
    while not stop():
        parent, other_parent = select_parents(generation)

def select_parents(generation):
    pass

def fitness(state):
    collisions = 0
    for queen in range(len(state)-1):
        for other_queen in range(queen, len(state)-1):
            if state[queen] == state[other_queen]:
                collisions += 1
            if state[queen]+other_queen <= len(state) and state[queen]+other_queen == state[other_queen]:
                collisions += 1
            if state[queen]-other_queen > 0 and state[queen]-other_queen == state[other_queen]:
                collisions += 1
    if collisions == 0:
        solutions.append(convert_board_to_tuple(state))
        solution_set.add(convert_board_to_tuple(state))
        print counter, "\t:",
        for i in solutions[len(solutions)-1]:
            print i, "\t",
        print " :", len(solution_set)
    return collisions

def random_parent(state):
    new_state = list(state)
    first = 0
    second = 0
    while first == second:
        first = random.randint(0,dimension-1)
        second = random.randint(0, dimension-1)
    first_list = new_state[first]
    second_list = new_state[second]
    new_state[first] = second_list
    new_state[second] = first_list
    if convert_board_to_tuple(new_state) in solutions:
        return random_state(state)
    return new_state

def stop():
    if dimension == 4:
        return len(solutions) >= 2
    elif dimension == 5:
        return len(solutions) >= 10
    elif dimension == 6:
        return len(solutions) >= 4
    elif dimension == 7:
        return len(solutions) >= 40
    elif dimension == 8:
        return len(solutions) >= 92
    elif dimension == 9:
        return len(solutions) >= 352
    elif dimension == 10:
        return len(solutions) >= 724
    elif dimension == 16:
        return len(solutions) >= 14772512
    elif dimension == 18:
        return len(solutions) >= 666090624
    elif dimension == 20:
        return len(solutions) >= 39029188884
    else:
        True

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
    for i in range(dimension):
        chess_board.append([])
        for j in range(dimension):
            chess_board[i].append('.')
    for i in range(dimension):
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
    for i in range(dimension):
        preprocessing.add(user_input[i])
    if dimension == len(preprocessing):
        return user_input
    for i in range(1, dimension+1):
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
dimension = len(user_input)
start = time.time()
init_board = preprocessing(user_input)
print_board(create_board(init_board))
simulated_annealing(init_board, 1000, 0.1)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start
