import config.constants as constants
import helpers.file as file_helper

class File:
    def __init__(self, filename: str, sheetname: str):
        self.file = file_helper.OpenPyxlReadExcel(filename)
        self.filename = filename
        self.sheetname = sheetname
        self._sheet = self.__load_sheet()

    def __load_sheet(self) -> any:
        sheet = self.file[self.sheetname]
        return sheet

    def loaded_workbook(self) -> any:
        return self.file

    def loaded_sheet(self) -> any:
        return self._sheet

    def get_filename(self) -> str:
        return self.filename

    def get_sheet_value(self, cellname: str) -> any:
        return self._sheet[cellname].value
    
    def get_max_row(self) -> int:
        return self._sheet.max_row
    
    def get_max_column(self) -> int:
        return self._sheet.max_column 