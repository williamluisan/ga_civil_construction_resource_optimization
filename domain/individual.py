from modules.file import File
from domain.general import *
import helpers.general as h_general
import config.constants as constants

class Individual:
    def create_first_individual(file: File) -> dict:
        result = {}

        for idx, row in enumerate(file.loaded_sheet().iter_rows()):
            row_number = idx + 1
            D_val = row[h_general.letter_to_array_index("D")].value
            E_val = row[h_general.letter_to_array_index("E")].value
            I_val = row[h_general.letter_to_array_index("I")].value
            J_val = row[h_general.letter_to_array_index("J")].value
            K_val = row[h_general.letter_to_array_index("K")].value
            L_val = row[h_general.letter_to_array_index("L")].value
            M_val = row[h_general.letter_to_array_index("M")].value
            if K_val is not None:
                K_val = K_val.strip()
                K_val_lower = K_val.lower()
            
            # check valid row to return
            valid_row = False
            if J_val == "OH":
                if K_val == "Pekerja":
                    valid_row = True
                    excel_row_number = row_number
                find_tukang = K_val_lower.find("tukang")
                if find_tukang != -1:
                    if K_val_lower != "kepala tukang":
                        valid_row = True

            # new value assignation for column
            if D_val is not None:
                D_val_value = D_val
            if E_val is not None:
                E_val_value = E_val

            # create initial individual and it's initial calculation
            # (data crawled from rows that met certain condition) 
            if valid_row:
                capability_of_one_day_work_per_one_worker, P_val = General.get_capability_of_one_worker_to_complete_in_one_day_compare_to_targeted_unit(
                    float(I_val), D_val_value
                )
                targeted_unit_amount = float(E_val_value)
                unit_defined_price = L_val
                rab_price = M_val

                total_of_workers = 1
                total_days_of_working = General.get_total_days_to_work_by_total_workers_compare_to_targeted_units(
                    capability_of_one_day_work_per_one_worker, total_of_workers, targeted_unit_amount
                )
                total_cost_by_unit_defined_price_and_total_of_workers = General.get_total_cost_by_unit_defined_price_and_total_of_workers(
                    unit_defined_price, total_of_workers
                )

                # row number as main index of the dictionary
                result[str(row_number)] = {
                    'type': K_val,
                    'excel_row_number': excel_row_number,
                    constants.E_COLUMN_INDEX_NAME: targeted_unit_amount,
                    constants.L_COLUMN_INDEX_NAME: unit_defined_price,
                    constants.M_COLUMN_INDEX_NAME: rab_price,
                    constants.O_COLUMN_INDEX_NAME: capability_of_one_day_work_per_one_worker,
                    constants.Q_COLUMN_INDEX_NAME: total_of_workers,
                    constants.R_COLUMN_INDEX_NAME: total_days_of_working,
                    constants.T_COLUMN_INDEX_NAME: total_cost_by_unit_defined_price_and_total_of_workers
                }
        
        return result