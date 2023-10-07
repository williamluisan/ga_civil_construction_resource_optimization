from domain.general import *
from domain.population import *
import config.constants as constants
import copy

class Solutions:
    def __init__(self, data: dict):
        self.data = data

    def create_random_solutions(self, total_solutions=constants.TOTAL_INDIVIDUAL_PER_POPULATION) -> list:
        return self.create_solutions(is_random=True, total_solutions=total_solutions)

    def create_solutions_one_worker_only_all_task(self) -> list:
        return self.create_solutions(is_random=False, total_worker=1, total_solutions=1)

    def create_solutions(self, is_random: bool, total_worker: int=1, total_solutions=constants.TOTAL_INDIVIDUAL_PER_POPULATION) -> list:
        data = self.data
        random_solutions = []
        total_solutions_to_generate = total_solutions

        for v in range(total_solutions_to_generate):
            solution_index = v + 1

            solution_data = copy.deepcopy(data)
            
            for v_data in solution_data:
                if is_random == True:
                    solution_to_mutate = solution_data[v_data]
                    randomized_total_of_workers = General.random_total_of_worker(solution_to_mutate)
                    total_of_workers_solution = randomized_total_of_workers
                if is_random == False:
                    total_of_workers_solution = total_worker

                solution_data[v_data][constants.Q_COLUMN_INDEX_NAME] = total_of_workers_solution

            random_solutions.append({
                "id": solution_index,
                "solution": solution_data
            })

        return random_solutions