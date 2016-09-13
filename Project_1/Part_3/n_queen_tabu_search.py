
from termcolor import colored
import sys
import time

#====== Algorithm =============================================================

def tabu_search(init_solution):
    global solution_set
    best_neighbor = init_solution
    short_term_memory = []
    intermediate_term_memory = {convert_board_to_tuple(init_solution): 1}
    long_term_memory = {convert_board_to_tuple(init_solution): 1}
    iteration = 0

    while not stop():
        iteration += 1
        if iteration > max_iterations:
            print "The maximum number of iterations is reached"
            break
        neighborhood = get_neighbors(best_neighbor)
        best_candidate = None
        for candidate in neighborhood:
            if convert_board_to_tuple(candidate) in short_term_memory:
                continue
            if convert_board_to_tuple(candidate) in long_term_memory:
                if long_term_memory[convert_board_to_tuple(candidate)] >= max_number_of_visits:
                    continue
            if best_candidate == None:
                best_candidate = candidate
            if fitness(best_candidate) >= fitness(candidate): #candidate has fewer hits
                best_candidate = candidate

            add_to_long_term_memories(best_candidate, intermediate_term_memory, long_term_memory)

        if best_candidate == None:
            best_candidate = create_board(intermediate_term_memory.keys()[0])
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
        memory.insert(0, convert_board_to_tuple(candidate))
    else:
        memory.insert(0, convert_board_to_tuple(candidate))
    return memory

def add_to_long_term_memories(best_candidate, intermediate_term_memory, long_term_memory):
    candidate_tuple = best_candidate
    if type(best_candidate) is list:
        candidate_tuple= convert_board_to_tuple(candidate_tuple)
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

def fitness(candidate):
    global solution_set
    global counter
    collisions = 0
    for col_queen in range(len(candidate)-1, 0, -1):
        for row_queen in range(len(candidate)):
            if candidate[row_queen][col_queen] == 'Q':
                for col in range(1, col_queen+1):
                    if row_queen-col >= 0 and candidate[row_queen-col][col_queen-col] == 'Q':
                        collisions += 1
                    if candidate[row_queen][col_queen-col] == 'Q':
                        collisions += 1
                    if row_queen+col < len(candidate) and candidate[row_queen+col][col_queen-col] == 'Q':
                        collisions += 1
    # print collisions
    if collisions == 0 and convert_board_to_tuple(candidate) not in solutions:
        solutions.append(convert_board_to_tuple(candidate))
        solution_set.add(convert_board_to_tuple(candidate))
        counter += 1
        print counter, ": ",
        for i in solutions[len(solutions)-1]:
            print i, " ",
        print " :", len(solution_set)
    return collisions

def get_neighbors(best_neighbor):
    return swap(best_neighbor)

def swap(best_neighbor):
    neighborhood = []
    for i in range(1, len(best_neighbor)):
        neighbor = list(best_neighbor)
        temp = neighbor[i]
        neighbor[i] = neighbor[i-1]
        neighbor[i-1] = temp
        neighborhood.append(neighbor)
    return neighborhood

# def random_swap(best_neighbor):
#     neighborhood = []
#     for i in range()

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


def convert_board_to_tuple(candidate):
    list_representation = []
    for col in range(len(candidate)):
        for row in range(len(candidate)):
            if candidate[row][col] == 'Q':
                list_representation.append(row+1)
    return tuple(list_representation)

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
max_tabu_memory_size = (len(user_input)/4)*3
max_number_of_visits = 2
max_iterations = 100000
counter = 0
solutions = []
solution_set = set()

start = time.time()
init_board = create_board(preprocessing(user_input))
print_board(init_board)
tabu_search(init_board)
print ""
print "Number of solutions: ", len(solutions)
print ""
end = time.time()
print end-start


#==============================================================================
