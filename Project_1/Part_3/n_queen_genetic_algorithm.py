
from termcolor import colored
import sys
import math
import random
import time

#====== Algorithm =============================================================

def genetic_algorithm(init_state, offspring_limit):
    #generation_number = 1
    generation = generate_init_population(init_state)
    while not stop():
        parent, other_parent = select_parents(generation)
        offspring = generate_offspring(parent, other_parent, offspring_limit)
        #evaluate_offspring(offspring)
        generation = offspring#generate_generation()
        #generation_number += 1

def select_parents(generation):
    fit_sum = 0
    prob_wheel = []
    for g in generation:
        fit_sum += (dimension-fitness(g))
    child = 0
    for i in range(fit_sum):
        fit = dimension-fitness(generation[child])
        for j in range(fit):
            prob_wheel.append(generation[child])
        if child < len(generation)-1:
            child += 1
        else:
            break
    random_parent_pos = random.randint(0, fit_sum-1)
    random_other_parent_pos = random.randint(0, fit_sum-1)
    parent = prob_wheel[random_parent_pos]
    other_parent = prob_wheel[random_other_parent_pos]
    while other_parent == parent:
        other_parent = prob_wheel[random.randint(0, fit_sum-1)]
    if len(solutions) < 1:
        print "Parent: ", parent, " other_parent: ", other_parent
    return parent, other_parent

def crossover(parent, other_parent):
    offspring = []
    offspring.extend(parent[:2])
    for i in other_parent:
        if i not in offspring:
            offspring.append(i)
    return offspring

def mutate(state):
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
    return tuple(new_state)

def generate_offspring(parent, other_parent, offspring_limit):
    offspring = []
    child = crossover(parent, other_parent)
    for o in range(10):
        offspring.append(mutate(child))
    return list(set(offspring))

def fitness(state):
    collisions = 0
    for queen_pos in range(len(state)-1):
        counter = 1
        up = False
        straight = False
        down = False
        for other_queen_pos in range(queen_pos+1, len(state)):
            if state[queen_pos] == state[other_queen_pos] and not straight:
                collisions += 1
                straight = True
            if state[queen_pos]+counter == state[other_queen_pos] and not up:
                collisions += 1
                up = True
            if state[queen_pos]-counter == state[other_queen_pos] and not down:
                collisions += 1
                down = True
            counter += 1
    if collisions == 0 and state not in solutions:
        solutions.append(state)
        solution_set.add(state)
        print len(solutions), "\t:",
        for i in solutions[len(solutions)-1]:
            print i, "\t",
        print " :", len(solution_set)
    return collisions

def generate_init_population(state):
    generation = []
    for i in range(6):
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
        generation.append(tuple(new_state))
    return generation

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
genetic_algorithm(init_board, 10)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start
