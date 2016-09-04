
from termcolor import colored

#====== Algorithm =============================================================

def tabu_search(init_solution):
    global solution_set
    best_neighbor = init_solution
    tabu_short_term_memory = []
    tabu_long_term_memory = {convert_list_to_string(init_solution): 1}

    while not stop():
        neighborhood = get_neighbors(best_neighbor)
        #print("bn", convert_list_to_string(best_neighbor))
        # for n in neighborhood:
        #     print(convert_list_to_string(n))
        #     print(fitness(n))
        # print
        best_candidate = None
        for candidate in neighborhood:
            if convert_list_to_string(candidate) in tabu_short_term_memory:
                #print("in tm")
                continue
            if best_candidate == None:
                best_candidate = candidate
            if fitness(best_candidate) >= fitness(candidate): #candidate has fewer hits
                best_candidate = candidate
            if convert_list_to_string(best_candidate) in tabu_long_term_memory:
                tabu_long_term_memory[convert_list_to_string(best_candidate)] += 1
            else:
                tabu_long_term_memory[convert_list_to_string(best_candidate)] = 1
        #print("bc: ", convert_list_to_string(best_candidate))
        tabu_short_term_memory = add_to_memory(convert_list_to_string(best_candidate), tabu_short_term_memory)
        # for i in tabu_short_term_memory:
        #     print convert_list_to_string(i)
        best_neighbor = best_candidate
    print "Done"

def add_to_memory(candidate, tabu_short_term_memory):
    memory = list(tabu_short_term_memory)
    if len(tabu_short_term_memory) == max_tabu_memory_size:
        memory = tabu_short_term_memory[:-1]
        memory.insert(0, candidate)
    else:
        memory.insert(0, candidate)
    return memory

def fitness(candidate):
    global solution_set
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
    if collisions == 0 and candidate not in solutions:
        solutions.append(convert_list_to_string(candidate))
        solution_set.add(convert_list_to_string(candidate))
        print "Solution: ", solutions[len(solutions)-1]
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

def stop():
    return len(solutions) >= 92

def convert_list_to_string(candidate):
    string = ""
    for col in range(len(candidate)):
        for row in range(len(candidate)):
            if candidate[row][col] == 'Q':
                string += `row+1`
    return string

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
    user_input = raw_input().replace(' ', '')
    return user_input

def preprocessing():
    pass # fixes so that no queen is on the same rownumber

max_tabu_memory_size = 1000
solutions = []
solution_set = set()
user_input = user_interaction()
init_board = create_board(user_input)
print_board(init_board)
tabu_search(init_board)
print len(solutions)
print len(solution_set)

#==============================================================================
