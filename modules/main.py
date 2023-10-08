from modules.file import File
from modules.libraries_example.pygad_ai_generated import Pygad
from modules.libraries_example.deap_ai_generated import Deap
from domain.general import *
from domain.population import *
from domain.individual import *
from domain.genetic_algorithm.solutions import *
from domain.genetic_algorithm.fitness_function import *
from domain.genetic_algorithm.selection import *
from domain.genetic_algorithm.crossover import *
from domain.genetic_algorithm.mutation import *
import config.constants as constants
import time

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    FitnessFunction = FitnessFunction()

    def execute():
        start_time = time.time()

        # the main index of the dictionary will be the excel row number
        first_individual = Individual.create_first_individual(Main.File)

        # create random solutions
        Solutions_mod = Solutions(first_individual)
        first_solution = Solutions_mod.create_random_solutions()
        Population_mod = Population(first_solution)
        first_solution = Population_mod.calculate_values_for_individual_fitness()

        # initial solution/recommendation
        solution = first_solution
        solution_data_structure_sample = solution[0] # the solution data structure sample is cloned from the very first random solution generated
        
        # get the initial optimum fitness solution, assuming 1 worker for each task is the best to press the cost
        # regardless the days will be spent
        solution_one_worker_only_all_task_create = Solutions_mod.create_solutions_one_worker_only_all_task()
        Population_mod = Population(solution_one_worker_only_all_task_create)
        solution_one_worker_only_all_task = Population_mod.calculate_fitness_result_and_efficiency_value()[0]
        assumed_best_solution_total_of_workers = solution_one_worker_only_all_task['result']['total_of_workers']
        assumed_max_total_days_of_working = solution_one_worker_only_all_task['result']['total_days_of_working']
        assumed_best_solution_total_cost_of_workers = solution_one_worker_only_all_task['result']['total_cost_of_workers']

        # GA loop starts (to find the best solution, then stop)
        population_counter = 0
        individual_counter = 0
        increment_id = []
        best_solution = None
        best_solution_efficiency_value = 0
        termination_threshold_counter = 0
        while True:
            ## fitness
            Population_mod = Population(solution)
            solution = Population_mod.calculate_fitness_result_and_efficiency_value(
                assumed_best_solution_total_of_workers = assumed_best_solution_total_of_workers
                , assumed_max_total_days_of_working = assumed_max_total_days_of_working
                , assumed_best_solution_total_cost_of_workers = assumed_best_solution_total_cost_of_workers
            )
            last_individual_increment_id = solution[-1]['id']
            increment_id.append(last_individual_increment_id)
            ## //
            
            ## selection
            Selection_mod = Selection(solution)
            solution_elitist, solution_selected_for_crossover = Selection_mod.run()
            
            # initiate new solution
            solution = solution_elitist
            ## //

            ## termination process
            possible_best_solution = copy.deepcopy(solution_elitist[0])
            possible_best_solution_efficiency_value = possible_best_solution['efficiency_value']

            # initiate first best solution efficiency value
            if population_counter == 0:
                best_solution_efficiency_value = possible_best_solution_efficiency_value

            if possible_best_solution_efficiency_value < best_solution_efficiency_value:
                best_solution = copy.deepcopy(possible_best_solution)
                best_solution_efficiency_value = best_solution['efficiency_value']
                termination_threshold_counter = 0
            else:
                if termination_threshold_counter == constants.TERMINATION_THRESHOLD:
                    end_time = time.time()
                    execution_time = end_time - start_time

                    print("Best solution found by reached the termination threshold.")
                    return execution_time, best_solution_efficiency_value, population_counter, individual_counter, best_solution
                
                termination_threshold_counter += 1
            ## //
            
            ## crossover
            Crossover_mod = Crossover(solution_selected_for_crossover, solution_data_structure_sample, last_individual_increment_id)
            crossover_result = Crossover_mod.run()

            # merge elitist solution and crossover result
            solution = solution + crossover_result
            ## //

            ## mutation
            Mutation_mod = Mutation(solution)
            solution = Mutation_mod.run()
            ## //

            population_counter += 1
            total_solution = len(solution)
            individual_counter += total_solution
        
    def execute_pygad():
        return Pygad.execute()

    def execute_deap():
        return Deap.execute()