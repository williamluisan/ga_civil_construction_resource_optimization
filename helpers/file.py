from openpyxl import load_workbook

def OpenPyxlReadExcel(filename: str) -> any:
    wb = load_workbook(filename)
    return wb