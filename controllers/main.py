import config.constants as constants
import helpers.file as file_helper

class Main:
    def execute():
        excel_file = file_helper.OpenPyxlReadExcel(constants.MAIN_EXCEL_FILENAME)
        print(excel_file)