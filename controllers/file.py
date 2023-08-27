import config.constants as constants
import helpers.file as file_helper

class File:
    def __init__(self, filename: str, sheetname: str):
        self.filename = filename
        self.sheetname = sheetname

    def __load_sheet(self) -> any:
        file = file_helper.OpenPyxlReadExcel(self.filename)
        sheet = file[self.sheetname]
        return sheet

    def get_sheet_value(self, cellname: str) -> any:
        sheet = self.__load_sheet()
        return sheet[cellname].value
