import pygad
import numpy

class Pygad:
    def execute():

        # Define the fitness function to optimize total workers, total days, and total cost
        def fitness_function(solution):
            total_of_workers = 0
            total_cost = 0
            for _, gene_values in solution.items():
                total_of_workers += gene_values.get("[Q]total_of_workers", 0)
                total_cost += gene_values.get("[T]total_cost_by_unit_defined_price_and_total_of_workers", 0)
            
            # Invert the total cost to minimize it
            fitness = 1 / total_cost
            
            return fitness
    
        # Define the data (replace this with your actual data)
        data = [
            {
                "id": 8,
                "solution": {
                    "259": {
                        "[E]targeted_unit_amount": 8,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 0.144,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "267": {
                        "[E]targeted_unit_amount": 5,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 12.345679012345679,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 0.045,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "275": {
                        "[E]targeted_unit_amount": 2,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 24.390243902439025,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 0.041,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    }
                },
                "result": {
                "total_of_workers": 150,
                "total_days_of_working": 482.24274535714284,
                "total_cost_of_workers": 16740000
                },
                "efficiency_value": 9.603330358474135
            },
            {
                "id": 3,
                "solution": {
                "259": {
                    "[E]targeted_unit_amount": 8,
                    "[L]unit_defined_price": 110000,
                    "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                    "[Q]total_of_workers": 3,
                    "[R]total_days_of_working": 0.09599999999999999,
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                },
                "267": {
                    "[E]targeted_unit_amount": 5,
                    "[L]unit_defined_price": 110000,
                    "[O]capability_of_one_day_work_per_one_worker": 12.345679012345679,
                    "[Q]total_of_workers": 8,
                    "[R]total_days_of_working": 0.050625,
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 880000
                },
                "275": {
                    "[E]targeted_unit_amount": 2,
                    "[L]unit_defined_price": 110000,
                    "[O]capability_of_one_day_work_per_one_worker": 24.390243902439025,
                    "[Q]total_of_workers": 2,
                    "[R]total_days_of_working": 0.041,
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                }
                },
                "result": {
                "total_of_workers": 168,
                "total_days_of_working": 220.2379108730159,
                "total_cost_of_workers": 18600000
                },
                "efficiency_value": 10.393964844211691
            },
            {
                "id": 1,
                "solution": {
                "259": {
                    "[E]targeted_unit_amount": 8,
                    "[L]unit_defined_price": 110000,
                    "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                    "[Q]total_of_workers": 8,
                    "[R]total_days_of_working": 0.036,
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 880000
                },
                "267": {
                    "[E]targeted_unit_amount": 5,
                    "[L]unit_defined_price": 110000,
                    "[O]capability_of_one_day_work_per_one_worker": 12.345679012345679,
                    "[Q]total_of_workers": 4,
                    "[R]total_days_of_working": 0.10125,
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                },
                "275": {
                    "[E]targeted_unit_amount": 2,
                    "[L]unit_defined_price": 110000,
                    "[O]capability_of_one_day_work_per_one_worker": 24.390243902439025,
                    "[Q]total_of_workers": 3,
                    "[R]total_days_of_working": 0.027333333333333334,
                    "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                }
                },
                "result": {
                "total_of_workers": 175,
                "total_days_of_working": 287.51283619047615,
                "total_cost_of_workers": 19340000
                },
                "efficiency_value": 10.875806611297863
            }
        ]

        # Assuming your data is stored in a variable called 'data'
        num_solutions = len(data)

        # Create an initial population of solutions (you can leave this empty or adjust as needed)
        initial_population = [{} for _ in range(num_solutions)]

        # Create an instance of the PyGAD optimizer
        ga = pygad.GA(num_generations=100,
              num_parents_mating=10,
              fitness_func=fitness_function,
              num_genes=num_solutions,  # Number of genes equals the number of solutions
              sol_per_pop=num_solutions,  # Population size equals the number of solutions
              initial_population=initial_population)

        # Start the optimization process
        ga.run()

        # Get the best solution and its fitness value
        best_solution, best_fitness = ga.output_dict['last_generation']['solution'], ga.output_dict['last_generation']['fitness']
        
        # Print the best solution and its fitness
        print("Best Solution:", best_solution)
        print("Best Fitness:", best_fitness)
