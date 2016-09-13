
from termcolor import colored
import sys
import math
import random
import time

#====== Algorithm =============================================================

def simulated_annealing(init_state, init_temp, temp_stop):
    temp = init_temp
    state = init_state
    while not stop():
        while temp > temp_stop:
            new_state = get_state(state)
            delta_E = fitness(state)-fitness(new_state)
            if delta_E < 0:
                state = new_state
            else:
                if prob_of_acceptance(fitness(new_state), temp):
                    state = new_state
            temp = temp_decay(temp)
        state = get_state(state)
        temp = init_temp

def get_state(state):
    return random_state(state)

def random_state(state):
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


def temp_decay(temp):
    return temp * 0.95

def prob_of_acceptance(delta_E, temp):
    return math.exp((-delta_E)/temp) > 0.2#random.uniform(0,1)

def fitness(state):
    global solution_set
    global counter
    collisions = 0
    for col_queen in range(len(state)-1, 0, -1):
        for row_queen in range(len(state)):
            if state[row_queen][col_queen] == 'Q':
                for col in range(1, col_queen+1):
                    if row_queen-col >= 0 and state[row_queen-col][col_queen-col] == 'Q':
                        collisions += 1
                    if state[row_queen][col_queen-col] == 'Q':
                        collisions += 1
                    if row_queen+col < len(state) and state[row_queen+col][col_queen-col] == 'Q':
                        collisions += 1
    if collisions == 0 and convert_board_to_tuple(state) not in solutions:
        solutions.append(convert_board_to_tuple(state))
        solution_set.add(convert_board_to_tuple(state))
        counter += 1
        print counter, ": ",
        for i in solutions[len(solutions)-1]:
            print i, " ",
        print ":", len(solution_set)
    return collisions

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

def convert_board_to_tuple(state):
    list_representation = []
    for col in range(len(state)):
        for row in range(len(state)):
            if state[row][col] == 'Q':
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
    if len(user_input) < 3:
        for i in range(int(user_input[0])):
            int_list.append(i+1)
    else:
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
init_board = create_board(preprocessing(user_input))
print_board(init_board)
simulated_annealing(init_board, 1000, 0.1)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start
