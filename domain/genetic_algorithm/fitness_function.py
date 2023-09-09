import helpers.general as h_general
import config.constants as constants

class FitnessFunction:
    def calculate(data: list) -> (int, float, float):
        sum_total_of_workers = sum_total_days_of_working = sum_total_cost_of_workers = 0

        solution = data["solution"]

        for v_data in solution:
            sum_total_of_workers += solution[v_data][constants.Q_COLUMN_INDEX_NAME]
            sum_total_days_of_working += solution[v_data][constants.R_COLUMN_INDEX_NAME]
            sum_total_cost_of_workers += solution[v_data][constants.T_COLUMN_INDEX_NAME]

        return sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers
    
    def calculate_efficiency_value(
        assumed_best_solution_total_of_workers: int,
        assumed_max_total_days_of_working: float,
        assumed_best_solution_total_cost_of_workers: float,
        total_of_workers: int,
        total_days_of_working: float,
        total_cost_of_workers: float
    ) -> float:
        """
        This function is to calculate and sum the efficiency value 
        from the given solution or the calculated fitness function, 
        the smaller the efficiency value means more efficient.

        efficiency value of total of worker: total_of_workers / assumed_best_solution_total_of_workers
        efficiency value of total days of working: total_days_of_working / assumed_max_total_days_of_working
        efficiency value of total cost of workers: total_cost_of_workers / assumed_best_solution_total_cost_of_workers

        Return:
            float: the sum of the efficiency value
        """
        ev_total_of_workers = total_of_workers / assumed_best_solution_total_of_workers
        ev_total_days_of_working = total_days_of_working / assumed_max_total_days_of_working
        ev_total_cost_of_workers = total_cost_of_workers / assumed_best_solution_total_cost_of_workers

        sum_result = ev_total_of_workers + ev_total_days_of_working + ev_total_cost_of_workers

        return sum_result
