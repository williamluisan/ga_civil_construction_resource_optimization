from modules.file import File
from domain.general import *
from domain.individual import *
from domain.genetic_algorithm.random_solutions import *
import config.constants as constants
import json

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file

    def execute():
        # the main index of the dictionary will be the excel row number
        first_individual = Individual.create_first_individual(Main.File)

        # create random solutions
        random_solutions = RandomSolutions(first_individual)
        first_solution = random_solutions.create_random_solutions()

        # GA loop starts (to find the best solution, then stop)
        solution = first_solution
        for v_solution in solution:
            print(solution[v_solution], end = "\n\n")

        # (debug)
        # pretty_print = json.dumps(random_solutions.create_random_solutions(), indent = 4)
        # print(pretty_print)
