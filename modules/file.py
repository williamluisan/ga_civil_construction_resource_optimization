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
    
    def write_solution_to_file(self, solution_to_write: dict, solution_result_to_write: dict) -> any:
        workbook = self.loaded_workbook()
        sheet = self.loaded_sheet()
        for v_stw in solution_to_write:
            O_cell_reference = f'O{v_stw}'
            Q_cell_reference = f'Q{v_stw}'
            R_cell_reference = f'R{v_stw}'
            S_cell_reference = f'S{v_stw}'
            T_cell_reference = f'T{v_stw}'
            O_cell_value = round(solution_to_write[v_stw][constants.O_COLUMN_INDEX_NAME], 2)
            R_cell_value = round(solution_to_write[v_stw][constants.R_COLUMN_INDEX_NAME], 2)
            sheet[O_cell_reference] = O_cell_value
            sheet[Q_cell_reference] = solution_to_write[v_stw][constants.Q_COLUMN_INDEX_NAME]
            sheet[R_cell_reference] = R_cell_value
            sheet[S_cell_reference] = constants.S_COLUMN_VALUE
            sheet[T_cell_reference] = solution_to_write[v_stw][constants.T_COLUMN_INDEX_NAME]
        sheet['W4'] = solution_result_to_write["total_of_workers"]
        sheet['W5'] = solution_result_to_write["total_days_of_working"]
        sheet['W6'] = solution_result_to_write["total_cost_of_workers"]
        workbook.save(self.get_filename())