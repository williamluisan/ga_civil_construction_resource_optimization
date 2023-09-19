from modules.file import File
from domain.general import *
from domain.individual import *
from domain.genetic_algorithm.solutions import *
from domain.genetic_algorithm.fitness_function import *
from domain.genetic_algorithm.selection import *
from modules.libraries.pygad_multi_objective import Pygad
from modules.libraries.deap_knapsack import Deap
import config.constants as constants
import helpers.general as h_general

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    FitnessFunction = FitnessFunction()

    def execute():
        # the main index of the dictionary will be the excel row number
        first_individual = Individual.create_first_individual(Main.File)
        
        # create random solutions
        Solutions_mod = Solutions(first_individual)
        first_solution = Solutions_mod.create_random_solutions()

        # initial solution/recommendation
        solution = first_solution

        # get the initial optimum fitness solution, assuming 1 worker for each task is the best to press the cost
        # regardless the days will be spent
        solution_one_worker_only_all_task_create = Solutions_mod.create_solutions_one_worker_only_all_task()
        solution_one_worker_only_all_task = []
        for v_solution_one_worker_only_all_task_create in solution_one_worker_only_all_task_create:
            sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers = FitnessFunction.calculate(
                v_solution_one_worker_only_all_task_create
            )
            v_solution_one_worker_only_all_task_create["result"] = {
                "total_of_workers": sum_total_of_workers,
                "total_days_of_working": sum_total_days_of_working,
                "total_cost_of_workers": sum_total_cost_of_workers,
            }
            solution_one_worker_only_all_task.append(v_solution_one_worker_only_all_task_create)
        
        assumed_best_solution_total_of_workers = sum_total_of_workers
        assumed_max_total_days_of_working = sum_total_days_of_working
        assumed_best_solution_total_cost_of_workers = sum_total_cost_of_workers

        # GA loop starts (to find the best solution, then stop)
        count = 0
        print = []
        while True:
            for k_solution, v_solution in enumerate(solution):
                # fitness function calculation
                sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers = FitnessFunction.calculate(v_solution)
                v_solution["result"] = {
                    "total_of_workers": sum_total_of_workers,
                    "total_days_of_working": sum_total_days_of_working,
                    "total_cost_of_workers": sum_total_cost_of_workers,
                }

                # efficiency value calculation
                efficency_value = FitnessFunction.calculate_efficiency_value(
                    assumed_best_solution_total_of_workers, assumed_max_total_days_of_working, assumed_best_solution_total_cost_of_workers
                    , sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers
                )
                v_solution["efficiency_value"] = efficency_value
                solution[k_solution] = v_solution

            Selection_mod = Selection(solution)
            solution_elitist = Selection_mod.get_elitist_solution()
            solution_selected_for_crossover = Selection_mod.get_selected_solution_for_crossover()

            # elitist rule for new generation
            solution = solution_elitist

            return solution
        
    def execute_pygad():
        Pygad.execute()

    def execute_deap():
        return Deap.execute()