import config.constants as constants

class Crossover:
    def __init__(self, data: dict):
        self.data = data

    def run(self) -> list:
        selected_solution_list = self.convert_selected_solution_to_list_of_total_of_workers()
        total_count_selected_solution_list = selected_solution_list.count(selected_solution_list)
        
        crossover_solution = []
        for i in selected_solution_list:


        return selected_solution_list

    def convert_selected_solution_to_list_of_total_of_workers(self) -> list:
        selected_solution = self.data 

        solution_list_of_total_of_workers = []
        all_solution_list_of_total_of_workers = []
        for i in selected_solution:
            for y in i['solution']:
                total_of_workers = i['solution'][y][constants.Q_COLUMN_INDEX_NAME]
                solution_list_of_total_of_workers.append(total_of_workers)
            all_solution_list_of_total_of_workers.append(solution_list_of_total_of_workers)

        return all_solution_list_of_total_of_workers