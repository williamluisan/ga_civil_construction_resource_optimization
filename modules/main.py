import config.constants as constants
import helpers.general as h_general
from modules.file import File
from domain.general import *
import json

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    
    def execute():
        # the main index of the dictionary will be the excel row number
        first_individual = {}

        for idx, row in enumerate(Main.File.loaded_sheet().iter_rows()):
            row_number = idx + 1
            D_val = row[h_general.letter_to_array_index("D")].value
            E_val = row[h_general.letter_to_array_index("E")].value
            I_val = row[h_general.letter_to_array_index("I")].value
            J_val = row[h_general.letter_to_array_index("J")].value
            K_val_value = row[h_general.letter_to_array_index("K")].value
            L_val = row[h_general.letter_to_array_index("L")].value
            if K_val_value is not None:
                K_val = K_val_value.strip()

            # create initial population and it's initial calculation
            # (data crawled from rows that met certain condition) 
            if J_val == "OH" and K_val == "Pekerja":
                capability_of_one_day_work_per_one_worker, P_val = General.get_capability_of_one_worker_to_complete_in_one_day_compare_to_targeted_unit(
                    float(I_val), D_val
                )
                targeted_unit_amount = E_val
                unit_defined_price = L_val

                total_of_workers = 1
                total_days_of_working = General.get_total_days_to_work_by_total_workers_compare_to_targeted_units(
                    capability_of_one_day_work_per_one_worker, total_of_workers, targeted_unit_amount
                )
                total_cost_by_unit_defined_price_and_total_of_workers = General.get_total_cost_by_unit_defined_price_and_total_of_workers(
                    unit_defined_price, total_of_workers
                )

                # row number as main index of the dictionary
                first_individual[str(row_number)] = {
                    "[O]capability_of_one_day_work_per_one_worker": 
                        h_general.format_float_two_decimal_points(capability_of_one_day_work_per_one_worker),
                    "[Q]total_of_workers": total_of_workers,
                    "[R]total_days_of_working": 
                        h_general.format_float_two_decimal_points(total_days_of_working),
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 
                        total_cost_by_unit_defined_price_and_total_of_workers
                }
        
        # (debug)
        # pretty_print = json.dumps(first_individual, indent = 4)
        # print(pretty_print)

        # create random solutions
        # ...
