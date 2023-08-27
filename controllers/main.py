import config.constants as constants
from controllers.file import File

class Main:
    def execute():
        # load the main file
        file = File(constants.MAIN_EXCEL_FILENAME, constants.MAIN_EXCEL_SHEET_NAME)
