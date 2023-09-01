import config.constants as constants
import helpers.general as h_general
from modules.file import File
from domain.general import *
import json

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    
    def execute():
        # the main index of the dictionary will be the excel row number
        initial_individual = {}

        for idx, row in enumerate(Main.File.loaded_sheet().iter_rows()):
            row_number = idx + 1
            B_val = row[h_general.letter_to_array_index("B")].value
            C_val = row[h_general.letter_to_array_index("C")].value
            D_val = row[h_general.letter_to_array_index("D")].value
            E_val = row[h_general.letter_to_array_index("E")].value
            I_val = row[h_general.letter_to_array_index("I")].value
            J_val = row[h_general.letter_to_array_index("J")].value
            K_val_value = row[h_general.letter_to_array_index("K")].value
            L_val = row[h_general.letter_to_array_index("L")].value
            if K_val_value is not None:
                K_val = K_val_value.strip()

            # create initial population (data crawled from rows that met certain condition) 
            if J_val == "OH" and K_val == "Pekerja":
                # row number as main index of the dictionary
                initial_individual[str(row_number)] = {
                    "total_of_workers": 1
                }
            
        print(json.dumps(initial_individual, indent = 4))
