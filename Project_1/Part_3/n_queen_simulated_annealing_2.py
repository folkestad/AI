
from termcolor import colored
import sys
import math
import random
import time

#====== Algorithm =============================================================

def simulated_annealing(init_state, init_temp, temp_stop):
    temp = init_temp
    state = init_state
    iteration = 0
    while not stop():
        while temp > temp_stop:
            iteration += 1
            new_state = get_state(state)
            solution_size = len(solutions)
            delta_E = fitness_tuple(state)-fitness_tuple(new_state)
            if delta_E < 0:
                if len(solutions) < 1:
                    print new_state
                state = new_state
            else:
                if prob_of_acceptance(fitness_tuple(new_state), temp):
                    if len(solutions) < 1:
                        print new_state
                    state = new_state
            if len(solutions) > solution_size:
                break
            temp = temp_decay(temp, iteration)
        state = get_state(state)
        temp = init_temp

def get_state(state):
    return random_state(state)

def random_state(state):
    new_state = list(state)
    first = random.randint(0,dimension-1)
    second = random.randint(0,dimension-1)
    while first == second:
        second = random.randint(0, dimension-1)
    first_list = new_state[first]
    second_list = new_state[second]
    new_state[first] = second_list
    new_state[second] = first_list
    while new_state in solutions:
        new_state = random_state(state)
    return tuple(new_state)

def random_state_2(state):
    new_state = list(state)
    first = random.randint(0,dimension-1)
    second = random.randint(0,dimension-1)
    third = random.randint(0,dimension-1)
    while first == second:
        second = random.randint(0, dimension-1)
    while first == third or second == third:
        third = random.randint(0, dimension-1)
    first_list = new_state[first]
    second_list = new_state[second]
    third_list = new_state[third]
    new_state[first] = third_list
    new_state[second] = first_list
    new_state[third] = second_list
    while new_state in solutions:
        new_state = random_state(state)
    return tuple(new_state)


def temp_decay(temp, iteration):
    return math.exp(-0.05*math.log1p(iteration))#temp * 0.95#math.exp(-0.05*math.log1p(iteration))

def prob_of_acceptance(delta_E, temp):
    return math.exp((-delta_E)/temp)*0.3 < random.random

def fitness_tuple(state):
    collisions = 0
    for queen_pos in range(len(state)-1):
        counter = 1
        for other_queen_pos in range(queen_pos+1, len(state)):
            if state[queen_pos] == state[other_queen_pos]:
                collisions += 1
            if state[queen_pos]+counter == state[other_queen_pos]:
                collisions += 1
            if state[queen_pos]-counter == state[other_queen_pos]:
                collisions += 1
            counter += 1
    if collisions == 0 and state not in solutions:
        solutions.append(state)
        solution_set.add(state)
        print len(solutions), "\t:",
        for i in solutions[len(solutions)-1]:
            print i, "\t",
        print " :", len(solution_set)
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
init_board = preprocessing(user_input)
print_board(create_board(init_board))
simulated_annealing(init_board, 1000, 0.25)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start
