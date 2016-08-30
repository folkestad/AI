
from termcolor import colored

#====== Algorithm =============================================================

def tabu_search():

    solution = None
    best_solution = solution
    tabu_list = []

    while not done():
        candidate_list = []
        best_candidate = None
        for solution_candidate in solution_neighborhood:
            if solution_candidate not in tabu_list and fitness(solution_candidate) > fitness(best_candidate):
                best_candidate = solution_candidate
                candidate_list.append(solution_candidate)
        solution = best_candidate
        if fitness(best_candidate) > fitness(best_solution):
            best_solution = best_candidate
        tabu_list.append(best_candidate)
        if len(tabu_list) > max_tabu_size:
            del tabu_list[0]
    return best_solution

#==============================================================================

#====== Creation of Board =====================================================

def user_interaction():
    print 'Place queens (ex. "2 4 6 0 0 0 0 0")'
    user_input = raw_input().replace(' ', '')
    return user_input

#==============================================================================

#====== Flow Controll =========================================================

user_input = user_interaction()

#==============================================================================
