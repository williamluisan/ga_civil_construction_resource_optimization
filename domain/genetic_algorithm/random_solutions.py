from domain.general import *
import config.constants as constants
import random
import helpers.general as h_general
import copy

class RandomSolutions:
    def __init__(self, data: dict):
        self.data = data

    def create_random_solutions(self):
        data = self.data

        random_solutions = {}

        for v in range(constants.TOTAL_INDIVIDUAL_PER_POPULATION):
            solution_index = v + 1

            solution_data = copy.deepcopy(data)

            for v_data in solution_data:
                targeted_unit_amount = solution_data[v_data][constants.E_COLUMN_INDEX_NAME]
                unit_defined_price = solution_data[v_data][constants.L_COLUMN_INDEX_NAME]
                capability_of_one_day_work_per_one_worker = solution_data[v_data][constants.O_COLUMN_INDEX_NAME]

                # TODO: random solution for total of workers per individual (chromosome)
                # should have more logic here, cannot mere a full random
                # ...
                total_of_workers_solution = random.randint(1, 10)
                
                # recalculate total days to work and total cost
                total_days_of_working = General.get_total_days_to_work_by_total_workers_compare_to_targeted_units(
                    capability_of_one_day_work_per_one_worker, total_of_workers_solution, targeted_unit_amount
                )
                total_cost_by_unit_defined_price_and_total_of_workers = General.get_total_cost_by_unit_defined_price_and_total_of_workers(
                    unit_defined_price, total_of_workers_solution
                )

                solution_data[v_data][constants.Q_COLUMN_INDEX_NAME] = total_of_workers_solution
                solution_data[v_data][constants.R_COLUMN_INDEX_NAME] = total_days_of_working
                solution_data[v_data][constants.T_COLUMN_INDEX_NAME] = total_cost_by_unit_defined_price_and_total_of_workers

            random_solutions[solution_index] = {"solution": solution_data}

        return random_solutions