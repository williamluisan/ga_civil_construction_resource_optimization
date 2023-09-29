class Population:
    def __init__(self, data: dict):
        self.data = data
    
    def calculate_values_for_individual_fitness(self) -> list:
        population = self.data

        solution_one_worker_only_all_task = []
        for v_population in population:
            sum_total_of_workers, sum_total_days_of_working, sum_total_cost_of_workers = FitnessFunction.calculate(
                v_solution_one_worker_only_all_task_create
            )
            v_solution_one_worker_only_all_task_create["result"] = {
                "total_of_workers": sum_total_of_workers,
                "total_days_of_working": sum_total_days_of_working,
                "total_cost_of_workers": sum_total_cost_of_workers,
            }
            solution_one_worker_only_all_task.append(v_solution_one_worker_only_all_task_create)