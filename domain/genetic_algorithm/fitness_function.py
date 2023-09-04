import helpers.general as h_general
import config.constants as constants

class FitnessFunction:
    def calculate(data: dict) -> (int, float, float):
        sum_total_of_workers = sum_total_days_of_working = sum_total_cost_of_workers = 0

        solution = data["solution"]

        for v_data in solution:
            sum_total_of_workers += solution[v_data][constants.Q_COLUMN_INDEX_NAME]
            sum_total_days_of_working += solution[v_data][constants.R_COLUMN_INDEX_NAME]
            sum_total_cost_of_workers += solution[v_data][constants.T_COLUMN_INDEX_NAME]

        return sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers