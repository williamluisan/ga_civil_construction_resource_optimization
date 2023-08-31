import config.constants as constants
import helpers.general as h_general
from modules.file import File
from domain.general import *

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    
    def execute():
        counter = 1;
        for row in Main.File.loaded_sheet().iter_rows():
            B_val = row[h_general.letter_to_array_index("B")].value
            C_val = row[h_general.letter_to_array_index("C")].value
            D_val = row[h_general.letter_to_array_index("D")].value
            E_val = row[h_general.letter_to_array_index("E")].value
            I_val = row[h_general.letter_to_array_index("I")].value
            J_val = row[h_general.letter_to_array_index("J")].value
            K_val_value = row[h_general.letter_to_array_index("K")].value
            if K_val_value is not None:
                K_val = K_val_value.strip()

            # do calculation if the row met the certain condition 
            # in this case (J col must be 'OH' and K col must be 'Pekerja')
            if J_val == "OH" and K_val == "Pekerja":
                capability_of_one_day_work_per_one_worker, P_val = General.get_capability_of_one_worker_to_complete_in_one_day_compare_to_targeted_unit(float(I_val), D_val)
                targeted_unit_amount = E_val
                O_val = h_general.format_float_two_decimal_points(capability_of_one_day_work_per_one_worker)

                ### generate random solutions should start from here
                total_of_workers = 1
                Q_val = total_of_workers
                total_days_of_working = General.get_total_days_to_work_by_total_workers_compare_to_targeted_unit(capability_of_one_day_work_per_one_worker, total_of_workers, targeted_unit_amount)
                R_val = h_general.format_float_two_decimal_points(total_days_of_working)
                
                print(f'{counter}| {B_val}. {C_val}: {O_val} {P_val} = {Q_val}/{R_val} Days', end = "\n")

                counter += 1
