from domain.genetic_algorithm.solutions import *
from domain.general import *
import config.constants as constants
import helpers.general as h_general
import numpy as np

class Mutation:
    def __init__(self, data: dict):
        self.data = data
        self.percentage_of_gen_to_mutate = constants.PERCENTAGE_OF_GEN_TO_MUTATE / 100

    def run(self) -> list:
        solutions = self.data
        
        for k_solutions, v_solutions in enumerate(solutions):
            solution = v_solutions['solution']
            solution_len = len(solution)
            solution_keys_list = list(solution.keys())
            total_solution_to_mutate = np.round(solution_len * self.percentage_of_gen_to_mutate).astype(int)

            # pick random solution key index inside an individual
            solution_key_index_to_mutate = []
            for i in range(total_solution_to_mutate):
                random_key_index = h_general.get_random_int_range_exclude_list_value(0, solution_len - 1, solution_key_index_to_mutate)
                solution_key_index_to_mutate.append(random_key_index)

            for j in solution_key_index_to_mutate:
                # solution_to_mutate = solutions[k_solutions]['solution'][solution_keys_list[j]]
                solution_to_mutate = solutions[k_solutions]['solution'][solution_keys_list[j]]
                randomized_total_of_workers = General.random_total_of_worker(solution_to_mutate)

                # mutation process starts here
                solutions[k_solutions]['solution'][solution_keys_list[j]][constants.Q_COLUMN_INDEX_NAME] = randomized_total_of_workers
        
        return solutions

