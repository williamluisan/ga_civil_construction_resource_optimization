from openpyxl import load_workbook

def OpenPyxlReadExcel(filename: str, data_only: bool = True) -> any:
    wb = load_workbook(filename, data_only = data_only)
    return wb