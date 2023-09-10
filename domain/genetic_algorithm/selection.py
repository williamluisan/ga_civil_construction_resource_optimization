import config.constants as constants
import math

class Selection:
    def __init__(self, data: dict):
        self.data = data

    def get_total_elitist_solution_inside_list_to_take(self) -> int:
        percentage = constants.ELITIST_SOLUTION_PERCENTAGE_TO_TAKE
        total_solution_per_population = constants.TOTAL_INDIVIDUAL_PER_POPULATION

        total = (percentage / 100) * total_solution_per_population

        return math.ceil(total)
        

    def sort_by_efficiency_value(self, sort: str="asc") -> list:
        data = self.data
        sorted_data = sorted(data, key=lambda x: x['efficiency_value'])

        return sorted_data

    def get_elitist_solution(self) -> list:
        # sort the given solution by efficiency value
        solution = self.sort_by_efficiency_value()

        total_to_take = self.get_total_elitist_solution_inside_list_to_take()

        return solution[:total_to_take]
    
    def get_selected_solution_for_crossover(self) -> list:
        # sort the given solution by efficiency value
        solution = self.sort_by_efficiency_value()

        total_to_take = self.get_total_elitist_solution_inside_list_to_take()

        return solution[total_to_take:]