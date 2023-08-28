import config.constants as constants
import helpers.general as h_general
from controllers.file import File

class Main:
    def execute():
        # load the main file
        file = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME)

        for row in file.loaded_sheet().iter_rows():
            J_val = row[h_general.letter_to_array_index("J")].value
            K_val = row[h_general.letter_to_array_index("K")].value

            print(f'{J_val} {K_val}')
