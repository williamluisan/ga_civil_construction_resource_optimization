import config.constants as constants
import helpers.file as file_helper

class File:
    def __init__(self, filename: str, sheetname: str):
        self.filename = filename
        self.sheetname = sheetname
        self._sheet = self.__load_sheet()

    def __load_sheet(self) -> any:
        file = file_helper.OpenPyxlReadExcel(self.filename)
        sheet = file[self.sheetname]
        return sheet
    
    def loaded_sheet(self) -> any:
        return self._sheet

    def get_sheet_value(self, cellname: str) -> any:
        return self._sheet[cellname].value
    
    def get_max_rows(self) -> int:
        return self._sheet.max_row