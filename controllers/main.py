import config.constants as constants
import helpers.general as h_general
from controllers.file import File
from domain.general import *

class Main:
    File = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME) # load the main file
    
    def execute():
        counter = 1;
        for row in Main.File.loaded_sheet().iter_rows():
            B_val = row[h_general.letter_to_array_index("B")].value
            C_val = row[h_general.letter_to_array_index("C")].value
            D_val = row[h_general.letter_to_array_index("D")].value
            I_val = row[h_general.letter_to_array_index("I")].value
            J_val = row[h_general.letter_to_array_index("J")].value
            K_val_value = row[h_general.letter_to_array_index("K")].value
            if K_val_value is not None:
                K_val = K_val_value.strip()

            # calculate total of workday compare to targeted unit for each row if met the certain condition
            if J_val == "OH" and K_val == "Pekerja":
                O_val, P_val = General.get_total_of_workday_compare_to_targeted_unit(float(I_val), D_val)
                O_val = format(O_val, ".2f")
                print(f'{counter}| {B_val}. {C_val}: {O_val} {P_val}', end = "\n")
                counter += 1
