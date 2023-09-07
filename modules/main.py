from modules.file import File
from domain.general import *
from domain.individual import *
from domain.genetic_algorithm.solutions import *
from domain.genetic_algorithm.fitness_function import *
import config.constants as constants
import helpers.general as h_general

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    FitnessFunction = FitnessFunction()

    def execute():
        # the main index of the dictionary will be the excel row number
        first_individual = Individual.create_first_individual(Main.File)

        Solutions_mod = Solutions(first_individual)

        # create random solutions
        first_solution = Solutions_mod.create_random_solutions()

        # initial solution/recommendation
        solution = first_solution

        # get the initial optimum fitness solution, assuming 1 worker for each task is the best to press the cost
        # regardless the days will be spent
        solution_one_worker_only_all_task = Solutions_mod.create_solutions_one_worker_only_all_task()
        for v_solution_one_worker_only_all_task in solution_one_worker_only_all_task:
            sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers = FitnessFunction.calculate(
                solution_one_worker_only_all_task[v_solution_one_worker_only_all_task]
            )
            solution_one_worker_only_all_task[v_solution_one_worker_only_all_task]["result"] = {
                "total_of_workers": sum_total_of_workers,
                "total_days_of_working": sum_total_days_of_working,
                "total_cost_of_workers": sum_total_cost_of_workers,
            }
        assumed_best_solution_total_of_workers = sum_total_of_workers
        assumed_max_total_days_of_working = sum_total_days_of_working
        assumed_best_solution_total_cost_of_workers = sum_total_cost_of_workers
        h_general.json_dumps_pretty_print(solution_one_worker_only_all_task)
        exit()

        # GA loop starts (to find the best solution, then stop)
        while True:
            for v_solution in solution:
                # fitness function calculation
                sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers = FitnessFunction.calculate(solution[v_solution])
                solution[v_solution]["result"] = {
                    "total_of_workers": sum_total_of_workers,
                    "total_days_of_working": sum_total_days_of_working,
                    "total_cost_of_workers": sum_total_cost_of_workers,
                }

                # efficiency value calculatino
                efficency_value = FitnessFunction.calculate_efficiency_value(
                    assumed_best_solution_total_of_workers, assumed_max_total_days_of_working, assumed_best_solution_total_cost_of_workers
                    , sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers
                )
                solution[v_solution]["efficiency_value"] = efficency_value

            h_general.json_dumps_pretty_print(solution)

            return
        
