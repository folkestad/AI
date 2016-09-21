
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
        iteration = 0
        while temp > temp_stop or not stop():
            if time.time()-start > 300:
                print "Timelimit reached for Simulated Annealing "
                print ""
                print "Number of solutions: ", len(solutions)
                print ""
                end = time.time()
                print "Time: ", end-start, "s"
                sys.exit(0)

            iteration += 1
            new_state = get_state(state, temp, init_temp)
            solution_size = solutions_length
            delta_E = fitness(state)-fitness(new_state)

            if delta_E < 0:
                if len(solutions) < 1:
                    print new_state
                state = new_state

            elif prob_of_acceptance(fitness(new_state), temp):
                    if len(solutions) < 1:
                        print new_state
                    state = new_state

            if solutions_length > solution_size:
                break

            temp = temp_decay(temp, iteration)

        iteration = 0
        temp = init_temp
        state = init_state

def get_state(state, temp, init_temp):
    return random_state_based_on_temp(state, temp, init_temp)

def temp_decay(temp, iteration):
    return math.exp(-0.2*math.log1p(iteration/temp))#temp*0.95#temp - 0.001##temp-0.01*iteration

def prob_of_acceptance(delta_E, temp):
    return math.exp((-delta_E)/temp)*0.6 < random.random()

# def random_state(state, temp, init_temp):
#     new_state = list(state)
#     first = random.randint(0,dimension-1)
#     second = random.randint(0,dimension-1)
#     while first == second:
#         second = random.randint(0, dimension-1)
#     first_list = new_state[first]
#     second_list = new_state[second]
#     new_state[first] = second_list
#     new_state[second] = first_list
#     while tuple(new_state) in solutions:
#         new_state = random_state(state, temp)
#     return tuple(new_state)

def random_state_based_on_temp(state, temp, init_temp):
    neighborhood = []
    pick_range = range(0, len(state))
    number_of_swaps = len(state)
    for i in range(number_of_swaps):
        new_state = list(state)
        if i > number_of_swaps/2:
            for i in range(2):
                row1 = random.choice(pick_range)
                row2 = random.choice(pick_range)
                while row1 == row2:
                    row2 = random.choice(pick_range)
                new_state[row1], new_state[row2] = new_state[row2], new_state[row1]
        else:
            for i in range(1):
                row1 = random.choice(pick_range)
                row2 = random.choice(pick_range)
                while row1 == row2:
                    row2 = random.choice(pick_range)
                new_state[row1], new_state[row2] = new_state[row2], new_state[row1]
        neighborhood.append(tuple(new_state))

    sorted_neighborhood = sorted(neighborhood, key=fitness)
    best_neighbor = sorted_neighborhood.pop(0)
    return best_neighbor

# def random_state_half_dimension(state, temp, init_temp):
#     neighborhood = []
#     pick_range = range(0, len(state))
#     for i in range(4):
#         new_state = list(state)
#         row1 = random.choice(pick_range)
#         row2 = random.choice(pick_range)
#         while row1 == row2:
#             row2 = random.choice(pick_range)
#         new_state[row1], new_state[row2] = new_state[row2], new_state[row1]
#         neighborhood.append(tuple(new_state))
#     sorted_neighborhood = sorted(neighborhood, key=fitness)
#     neighbor = sorted_neighborhood.pop()
#     while tuple(new_state) in solutions and sorted_neighborhood:
#         neighbor = sorted_neighborhood.pop()
#     return neighbor



# def random_state_neighborhood(state, temp):
#     neighborhood = []
#
#     new_state = list(state)
#     first = random.randint(0,dimension-1)
#     second = random.randint(0,dimension-1)
#     while first == second:
#         second = random.randint(0, dimension-1)
#     first_list = new_state[first]
#     second_list = new_state[second]
#     new_state[first] = second_list
#     new_state[second] = first_list
#     while tuple(new_state) in solutions:
#         new_state = random_state(state, temp)
#     return tuple(new_state)
#
# def random_state_2(state, temp, init_temp):
#     neighborhood = []
#     for i in range(1, len(state)):
#         neighbor = list(state)
#         neighbor[i], neighbor[i-1] = neighbor[i-1], neighbor[i]
#         neighborhood.append(tuple(neighbor))
#     sorted_neighborhood = sorted(neighborhood, key=fitness)
#     neighbor = sorted_neighborhood.pop()
#     while neighbor in solutions and sorted_neighborhood:
#         neighbor = sorted_neighborhood.pop()
#     return neighborhood.pop()

# def pick_best_in_neighborhood(state, temp, init_temp):
#     neighborhood = []
#     number_of_rows = range(0, len(state))
#     while len(number_of_rows) > 1:
#         swap_state = list(state)
#         row1 = random.choice(number_of_rows)
#         number_of_rows.remove(row1)
#         row2 = random.choice(number_of_rows)
#         number_of_rows.remove(row2)
#         swap_state[row1], swap_state[row2] = swap_state[row2], swap_state[row1]
#         neighborhood.append(tuple(swap_state))
#     sorted_neighborhood = sorted(neighborhood, key=fitness)
#     best_neighbor = sorted_neighborhood.pop()
#     while best_neighbor in solutions and sorted_neighborhood:
#         best_neighbor = sorted_neighborhood.pop()
#     return best_neighbor

def fitness(state):
    global solutions_length
    if state in visited:
        return visited[state]
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
    if collisions == 0 and state in solutions:
        return collisions
    if collisions == 0:
        solutions_length += 1
        solutions[state] = True
        #solution_set.add(state)
        print len(solutions), ":",
        for i in state:
            print i,
        print ""
    visited[state] = collisions
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

# def user_interaction():
#     print 'Place queens (ex. "2 4 6 3 1 8 7 5")'
#     user_input = raw_input().split(' ')
#     int_list = []
#     if len(user_input) < 3:
#         for i in range(int(user_input[0])):
#             int_list.append(i+1)
#     else:
#         for i in user_input:
#             int_list.append(int(i))
#     return tuple(int_list)

def user_interaction():
    global dimension
    print 'dimension (n)?'
    dimension = int(raw_input())
    print 'Place queens (ex. "2 4 6 3 1 8 7 5")'
    user_input = raw_input().split(' ')
    try:
        int_list = list(set([int(i) for i in user_input]))
    except:
        int_list = []
    print int_list

    if len(int_list) < dimension:
        unused = range(1, dimension+1)
        for i in int_list:
            unused.remove(i)
        for i in range(len(unused)):
            int_list.append(unused[0])
            unused.remove(unused[0])
    else:
        for i in int_list:
            int_list.append(i)
    print int_list
    return tuple(int_list)

# def preprocessing(user_input):
#     # fixes so that no queen is on the same rownumber
#     preprocessing = set()
#     for i in range(dimension):
#         if user_input[i] != 0:
#             preprocessing.add(user_input[i])
#     if dimension == len(preprocessing):
#         return user_input
#     for i in range(1, dimension+1):
#         if i not in preprocessing:
#             character = str(i).encode('utf-8')
#             preprocessing.add(int(character))
#     preprocessing = tuple(preprocessing)
#     return preprocessing

dimension = None
init_board = user_interaction()
max_number_of_visits = 4
counter = 0
solution_size = 0
solutions_length = 0
solutions = {}
visited = {}
solution_set = set()
start = time.time()
#init_board = preprocessing(user_input)
print_board(create_board(init_board))
simulated_annealing(init_board, 200, 0.5)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print "Time: ", end-start, "s"
