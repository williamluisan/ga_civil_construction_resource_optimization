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
    
    def convert_selected_solution_to_list_of_total_of_workers(self) -> list:
        selected_solution = self.get_selected_solution_for_crossover()

        solution_list_of_total_of_workers = []
        all_solution_list_of_total_of_workers = []
        for i in selected_solution:
            for y in i['solution']:
                total_of_workers = i['solution'][y][constants.Q_COLUMN_INDEX_NAME]
                solution_list_of_total_of_workers.append(total_of_workers)
            all_solution_list_of_total_of_workers.append(solution_list_of_total_of_workers)

        return all_solution_list_of_total_of_workers