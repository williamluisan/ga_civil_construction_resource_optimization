from domain.general import *
from domain.genetic_algorithm.fitness_function import *
import config.constants as constants
import random

class Population:
    def __init__(self, data: dict):
        self.data = data
    
    def calculate_values_for_individual_fitness(self) -> list:
        population = self.data
        population_recalculated = []
        
        for v_population in population:
            solution_data = v_population['solution']
            for v_data in solution_data:
                total_of_workers_solution = solution_data[v_data][constants.Q_COLUMN_INDEX_NAME]
                targeted_unit_amount = solution_data[v_data][constants.E_COLUMN_INDEX_NAME]
                unit_defined_price = solution_data[v_data][constants.L_COLUMN_INDEX_NAME]
                capability_of_one_day_work_per_one_worker = solution_data[v_data][constants.O_COLUMN_INDEX_NAME]

                # recalculate total days to work and total cost
                total_days_of_working = General.get_total_days_to_work_by_total_workers_compare_to_targeted_units(
                    capability_of_one_day_work_per_one_worker, total_of_workers_solution, targeted_unit_amount
                )
                total_cost_by_unit_defined_price_and_total_of_workers = General.get_total_cost_by_unit_defined_price_and_total_of_workers(
                    unit_defined_price, total_of_workers_solution
                )

                solution_data[v_data][constants.Q_COLUMN_INDEX_NAME] = total_of_workers_solution
                solution_data[v_data][constants.R_COLUMN_INDEX_NAME] = total_days_of_working
                solution_data[v_data][constants.T_COLUMN_INDEX_NAME] = total_cost_by_unit_defined_price_and_total_of_workers
            
            v_population['solution'] = solution_data

            population_recalculated.append(v_population)
        
        return population_recalculated
    
    def calculate_fitness_result_and_efficiency_value(self
        , assumed_best_solution_total_of_workers: float = 0
        , assumed_max_total_days_of_working: float = 0
        , assumed_best_solution_total_cost_of_workers: float = 0
    ) -> list:
        # calculate values for individual fitness first
        population = self.calculate_values_for_individual_fitness()
        
        population_with_result = []
        
        for v_solution in population:
            # fitness function calculation
            sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers = FitnessFunction.calculate(
                v_solution
            )
            v_solution["result"] = {
                "total_of_workers": sum_total_of_workers,
                "total_days_of_working": sum_total_days_of_working,
                "total_cost_of_workers": sum_total_cost_of_workers,
            }

            if assumed_best_solution_total_of_workers != 0 and assumed_max_total_days_of_working != 0 and assumed_best_solution_total_cost_of_workers != 0:
                # efficiency value calculation
                efficiency_value = FitnessFunction.calculate_efficiency_value(
                    assumed_best_solution_total_of_workers, assumed_max_total_days_of_working, assumed_best_solution_total_cost_of_workers
                    , sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers
                )
                v_solution["efficiency_value"] = efficiency_value

            population_with_result.append(v_solution)

        return population_with_result