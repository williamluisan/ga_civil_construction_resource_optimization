from modules.file import File
from domain.general import *
from domain.individual import *
from domain.genetic_algorithm.random_solutions import *
from domain.genetic_algorithm.fitness_function import *
import config.constants as constants
import helpers.general as h_general

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    FitnessFunction = FitnessFunction()

    def execute():
        # the main index of the dictionary will be the excel row number
        first_individual = Individual.create_first_individual(Main.File)

        # create random solutions
        random_solutions = RandomSolutions(first_individual)
        first_solution = random_solutions.create_random_solutions()
        
        # initial solution/recommendation
        solution = first_solution
        sum_total_of_workers = 999999999
        sum_total_days_of_working = 999999999
        sum_total_cost_of_workers = 999999999

        # GA loop starts (to find the best solution, then stop)
        while True:
            for v_solution in solution:
                solution_with_fitness_function = FitnessFunction.calculate_fitness_function(solution[v_solution])
                return
            return
