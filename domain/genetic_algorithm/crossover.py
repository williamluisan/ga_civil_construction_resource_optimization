import config.constants as constants

class Crossover:
    def __init__(self, data: dict):
        self.data = data

    def run(self) -> list:
        selected_solution_list = self.convert_selected_solution_to_list_of_total_of_workers()
        total_count_selected_solution_list = selected_solution_list.count(selected_solution_list)
        half_length_of_solution = len(selected_solution_list[0]) // 2

        crossover_solution = []
        for k, v_solution in enumerate(selected_solution_list):
            if k % 2 != 0:
                solution_parent_a = selected_solution_list[k]
                solution_parent_b = selected_solution_list[k + 1] 
                
                offspring_one = solution_parent_a[:half_length_of_solution] + solution_parent_b[half_length_of_solution:]
                offspring_two = solution_parent_a[half_length_of_solution:] + solution_parent_b[:half_length_of_solution]
                
                crossover_solution.append(offspring_one)
                crossover_solution.append(offspring_two)

        return selected_solution_list, crossover_solution

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