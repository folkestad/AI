
import sys
import math
import random
import time
import itertools

#====== Algorithm =============================================================

def genetic_algorithm(init_state, population_size, number_of_parents, mutation_rate):
    population = generate_init_population(init_state, population_size)
    generation_number = 0
    while not stop():
        if time.time()-start > 300:# or generation_number >= generation_number_stop:
            print "Reached timelimit for Genetic Algorithm "
            print ""
            print "Number of solutions: ", len(solutions)
            print ""
            print "Number of Generations: ", generation_number
            end = time.time()
            print "Time: ", end-start, "s"
            break
        if len(solutions) < 1 and generation_number%100 == 0:
            print "Generation: ", generation_number," - ", time.time()-start
            for p in population:
                print p, " "
            print ""
        parent_list = select_parents_favor_best(population, number_of_parents)
        offspring = generate_offspring(population, parent_list, mutation_rate, crossover_random)
        population = evaluate_offspring(offspring, parent_list, population_size)
        generation_number+=1

def generate_offspring(population, parent_list, mutation_rate, crossover_function):
    offspring = []
    not_visited = range(0,len(parent_list))
    while 0 < len(not_visited):
        p1 = random.choice(not_visited)
        not_visited.remove(p1)
        p2 = random.choice(not_visited)
        not_visited.remove(p2)
        child = crossover_function(parent_list[p1], parent_list[p2])
        if random.random() > mutation_rate:
            offspring.append(mutate(child))
        else:
            offspring.append(child)
        siblings = 9
        while siblings > 0:
            sibling = mutate(child)
            if sibling not in offspring:
                offspring.append(sibling)
            siblings-=1
    for o in offspring:
        if o in population:
            offspring.remove(o)
    return offspring

def generate_init_population(state, population_size):
    population = [tuple(state)]
    for i in xrange(1, population_size):
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
        population.append(tuple(new_state))
    return population

# def select_parents(population, number_of_parents):
#     fit_sum = 0
#     prob_wheel = []
#     parent_list = []
#     for p in population:
#         fit_sum += (dimension-fitness(p))
#     child = 0
#     for i in range(fit_sum):
#         fit = (dimension-fitness(population[child]))
#         for j in range(fit):
#             prob_wheel.append(population[child])
#         if child < len(population)-1:
#             child += 1
#         else:
#             break
#     while len(parent_list) != number_of_parents:
#         random_parent_pos = random.randint(0, len(prob_wheel)-1)
#         if random_parent_pos in solutions:# or random_parent_pos in visited:
#              continue
#         #print "wheel ", len(prob_wheel), " random_parent_pos ", random_parent_pos
#         parent_list.append(prob_wheel[random_parent_pos])
#     return parent_list

def select_parents_favor_best(population, number_of_parents):
    sorted_population = sorted(population, key=fitness)
    return sorted_population[:number_of_parents]

def evaluate_offspring(offspring, parent_list, population_size):
    sorted_offspring = sorted(offspring, key=fitness)
    population = parent_list[:]
    i = 0
    while len(population) < population_size:
        population.append(sorted_offspring[i])
        i+=1
    return population

# def crossover(parent, other_parent):
#     offspring = []
#     offspring.extend(parent[:len(parent)/4])#(len(parent)-1)/random.randint(1,len(parent)-1)])
#     for i in range(len(other_parent)):
#         print len(other_parent)
#         if other_parent[i] not in offspring:
#             offspring.append(i)
#     return tuple(offspring)

# def crossover_fitness_favoring(parent, other_parent):
#     offspring = []
#     p1 = parent
#     p2 = other_parent
#     if fitness(parent) < fitness(other_parent):
#         p1 = other_parent
#         p2 = parent
#     offspring.extend(p1[:len(parent)/3])
#     for i in p2:
#         if i not in offspring:
#             offspring.append(i)
#     return tuple(offspring)

def crossover_keep_equal(parent, other_parent):
    offspring = []
    missing = []
    for i in xrange(len(parent)):
        if parent[i] == other_parent[i]:
            offspring.append(parent[i])
        else:
            offspring.append(0)
            missing.append(parent[i])
    for i in xrange(len(offspring)):
        if offspring[i] == 0:
            offspring[i] = random.choice(missing)
            missing.remove(offspring[i])
    return tuple(offspring)

# def crossover_keep_equal_all_combos(parent, other_parent):
#     offspring = []
#     missing = []
#     all_offspring = []
#     positions = []
#     for i in xrange(len(parent)):
#         if parent[i] == other_parent[i]:
#             offspring.append(parent[i])
#         else:
#             offspring.append(0)
#             missing.append(parent[i])
#             positions.append(i)
#     permutations_of_missing = list(itertools.permutations(missing))
#     for i in xrange(len(permutations_of_missing)):
#         o = list(offspring)
#         for j in range(len(missing)):
#             o[positions[j]] = permutations_of_missing[i][j]
#         all_offspring.append(tuple(o))
#     # if len(set(offspring)) < len(set(parent)):
#     #     sys.exit(0)
#     return all_offspring

def crossover_random(parent, other_parent):
    crosspoint = random.randint(0,len(parent)-1)
    unused = range(1, len(parent)+1)
    left = list(parent[:crosspoint])
    for i in range(len(left)):
        unused.remove(left[i])
    right = list(other_parent[crosspoint:])
    for i in range(len(right)):
        if right[i] in unused:
            unused.remove(right[i])
    for i in range(len(right)):
        if right[i] in left:
            right[i] = random.choice(unused)
            unused.remove(right[i])
    left.extend(right)
    return tuple(left)

def mutate(state):
    new_state = list(state)
    first = 0
    second = 0
    while first == second:
        first = random.randint(0,dimension-1)
        second = random.randint(0, dimension-1)
    new_state[first], new_state[second] = new_state[second], new_state[first]
    return tuple(new_state)

def fitness(state):
    collisions = 0
    if state in visited:
        return visited[state]
    else:
        for queen_pos in xrange(len(state)-1):
            counter = 1
            for other_queen_pos in xrange(queen_pos+1, len(state)):
                if state[queen_pos] == state[other_queen_pos]:
                    collisions += 1
                if state[queen_pos]+counter == state[other_queen_pos]:
                    collisions += 1
                if state[queen_pos]-counter == state[other_queen_pos]:
                    collisions += 1
                counter += 1
        visited[state] = collisions
        if collisions == 0 and state not in solutions:
            solutions.append(state)
            #solution_set.add(state)
            print len(solutions), ": ",
            for i in solutions[len(solutions)-1]:
                print i,
            print ""#print ":", len(solution_set)
        return visited[state]
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

#====== Printing of Board and Helping methods =================================

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


# solution_set = set()
dimension = None
init_board = user_interaction()
population_size = 60
number_of_parents = population_size/2
if number_of_parents%2 != 0:
    number_of_parents+=1
mutation_rate = 0.8
generation_number_stop = 20000
counter = 0
solutions = []
visited = {}
start = time.time()
#init_board = preprocessing(user_input)
print_board(create_board(init_board))
genetic_algorithm(init_board, population_size, number_of_parents, mutation_rate)
# print ""
# print "Number of solutions: ", len(solutions)
# print ""
# end = time.time()
# print "Time: ", end-start, "s"
