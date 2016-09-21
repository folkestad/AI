
from termcolor import colored
import sys
import time

#====== Algorithm =============================================================

def tabu_search(init_solution):
    global solution_set
    best_neighbor = init_solution
    short_term_memory = []
    intermediate_term_memory = {init_solution: 1}
    long_term_memory = {init_solution: 1}
    iteration = 0

    while not stop():
        iteration += 1
        if time.time()-start > 300:
            print "Timelimit is reached"
            break
        neighborhood = get_neighbors(best_neighbor)
        best_candidate = None
        for candidate in neighborhood:
            if len(solutions) < 1:
                print candidate
            if candidate in short_term_memory:
                continue
            if candidate in long_term_memory:
                if long_term_memory[candidate] >= max_number_of_visits:
                    continue
            if best_candidate == None:
                best_candidate = candidate
            if fitness_tuple(best_candidate) >= fitness_tuple(candidate): #candidate has fewer hits
                best_candidate = candidate

            add_to_long_term_memories(best_candidate, intermediate_term_memory, long_term_memory)

        if best_candidate == None:
            best_candidate = intermediate_term_memory.keys()[0]
            add_to_long_term_memories(intermediate_term_memory.keys()[0], intermediate_term_memory, long_term_memory)
            if best_candidate == None:
                print "\nCould not find any more solutions with the current memory settings."
                sys.exit(0)

        short_term_memory = add_to_short_term_memory(best_candidate, short_term_memory)
        best_neighbor = best_candidate
    print ""
    print "Done"

def add_to_short_term_memory(candidate, short_term_memory):
    memory = list(short_term_memory)
    if len(short_term_memory) == max_tabu_memory_size:
        memory = short_term_memory[:-1]
        memory.insert(0, candidate)
    else:
        memory.insert(0, candidate)
    return memory

def add_to_long_term_memories(best_candidate, intermediate_term_memory, long_term_memory):
    candidate_tuple = best_candidate
    if type(best_candidate) is list:
        candidate_tuple= tuple(candidate_tuple)
    if candidate_tuple in intermediate_term_memory:
        if intermediate_term_memory[candidate_tuple] < max_number_of_visits:
            intermediate_term_memory[candidate_tuple] += 1
        else:
            del intermediate_term_memory[candidate_tuple]
    else:
        if candidate_tuple not in long_term_memory:
            intermediate_term_memory[candidate_tuple] = 1
    if candidate_tuple in long_term_memory:
        long_term_memory[candidate_tuple] += 1
    else:
        long_term_memory[candidate_tuple] = 1

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

def get_neighbors(best_neighbor):
    return swap_even_more(best_neighbor)

# def swap(best_neighbor):
#     neighborhood = []
#     for i in range(1, len(best_neighbor)):
#         neighbor = list(best_neighbor)
#         temp = neighbor[i]
#         neighbor[i] = neighbor[i-1]
#         neighbor[i-1] = temp
#         neighborhood.append(tuple(neighbor))
#     return neighborhood

def swap_even_more(best_neighbor):
    neighborhood = []
	# Swap rows
    for i in range(0, dimension - 1):
        for j in range(i + 1, dimension):
            neighbor = list(best_neighbor)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighborhood.append(tuple(neighbor))
    return neighborhood

def stop():
    if len(user_input) == 4:
        return len(solutions) >= 2
    elif len(user_input) == 5:
        return len(solutions) >= 10
    elif len(user_input) == 6:
        return len(solutions) >= 4
    elif len(user_input) == 7:
        return len(solutions) >= 40
    elif len(user_input) == 8:
        return len(solutions) >= 92
    elif len(user_input) == 9:
        return len(solutions) >= 352
    elif len(user_input) == 10:
        return len(solutions) >= 724
    elif len(user_input) == 16:
        return len(solutions) >= 14772512
    elif len(user_input) == 18:
        return len(solutions) >= 666090624
    elif len(user_input) == 20:
        return len(solutions) >= 39029188884
    else:
        True

#==============================================================================

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

user_input = user_interaction()
dimension = len(user_input)
max_tabu_memory_size = (len(user_input)/4)*3
max_number_of_visits = 2
max_iterations = 100000
counter = 0
solutions = []
solution_set = set()

start = time.time()
init_board = preprocessing(user_input)
print_board(create_board(init_board))
tabu_search(init_board)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start


#==============================================================================
