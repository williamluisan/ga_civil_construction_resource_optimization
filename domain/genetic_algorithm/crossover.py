import config.constants as constants
import copy

class Crossover:
    def __init__(self, data: dict, solution_data_structure_sample: dict, last_individual_increment_id: int = 0):
        """
        Args:
            data (dict)
            solution_data_structure_sample (dict): this variable purpose is to get known the desired final data structure to built
        """
        self.data = data
        self.solution_data_structure_sample = solution_data_structure_sample
        self.last_individual_increment_id = last_individual_increment_id

    def run(self) -> list:
        last_individual_increment_id = self.last_individual_increment_id

        solution_data_structure_sample = self.solution_data_structure_sample
        selected_solution_list = self.convert_selected_solution_to_list_of_total_of_workers()
        total_count_selected_solution_list = len(selected_solution_list)
        half_length_of_solution = len(selected_solution_list[0]) // 2

        crossover_solution = []
        have_last_individual_dont_have_mate = False
        for k, v_solution in enumerate(selected_solution_list):
            solution_parent_a = solution_parent_b = []
            offspring_one = offspring_two = []
            
            # check have individual that doesn't got mate match it with the very first individual
            if k == (total_count_selected_solution_list - 1):
                have_last_individual_dont_have_mate = True
                solution_parent_a = selected_solution_list[0]
                solution_parent_b = selected_solution_list[k]

            # crossover 2 parents side by side
            if have_last_individual_dont_have_mate == False:
                if k % 2 == 0:
                    solution_parent_a = selected_solution_list[k]
                    solution_parent_b = selected_solution_list[k + 1] 

            if solution_parent_a and solution_parent_b:
                offspring_one = solution_parent_a[:half_length_of_solution] + solution_parent_b[half_length_of_solution:]
                offspring_two = solution_parent_b[:half_length_of_solution] + solution_parent_a[half_length_of_solution:]
            
            if offspring_one and offspring_two:
                if have_last_individual_dont_have_mate == False:
                    crossover_solution.append(offspring_one)
                    crossover_solution.append(offspring_two)
                if have_last_individual_dont_have_mate == True:
                    if len(crossover_solution) != total_count_selected_solution_list:
                        # take the first offspring of matching the single last individual
                        crossover_solution.append(offspring_one)

        # set up the crossover solution to the main data structure
        crossover_solution_structured = []
        temp_crossover_solution_structured = {}
        for v_crossover_solution in crossover_solution:
            last_individual_increment_id += 1
            temp_crossover_solution_structured = copy.deepcopy(solution_data_structure_sample)
            temp_crossover_solution_structured['id'] = last_individual_increment_id
            for k, v in enumerate(temp_crossover_solution_structured['solution']):
                temp_crossover_solution_structured['solution'][v][constants.Q_COLUMN_INDEX_NAME] = v_crossover_solution[k]
            
            crossover_solution_structured.append(temp_crossover_solution_structured)
            
        return crossover_solution_structured

    def convert_selected_solution_to_list_of_total_of_workers(self) -> list:
        selected_solution = self.data 
        
        all_solution_list_of_total_of_workers = []
        for i in selected_solution:
            solution_list_of_total_of_workers = []      
            for y in i['solution']:
                total_of_workers = i['solution'][y][constants.Q_COLUMN_INDEX_NAME]
                solution_list_of_total_of_workers.append(total_of_workers)
            all_solution_list_of_total_of_workers.append(solution_list_of_total_of_workers)

        return all_solution_list_of_total_of_workers