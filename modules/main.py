from modules.file import File
from domain.general import *
from domain.individual import *
import config.constants as constants
import json

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    
    def execute():
        # the main index of the dictionary will be the excel row number
        first_individual = Individual.create_initial_individual(Main.File)
        
        # (debug)
        pretty_print = json.dumps(first_individual, indent = 4)
        print(pretty_print)

        # create random solutions
        # ...
