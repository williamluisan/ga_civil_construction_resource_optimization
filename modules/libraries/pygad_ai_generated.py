import pygad
import numpy

class Pygad:
    def execute():

        # Define the fitness function to optimize total workers, total days, and total cost
        def fitness_function(solution):
            total_workers = 0
            total_days = 0
            total_cost = 0

            for task_id, task_params in solution.items():
                total_workers += task_params['[Q]total_of_workers']
                total_days += task_params['[R]total_days_of_working']
                total_cost += task_params['[T]total_cost_by_unit_defined_price_and_total_of_workers']

            # We want to minimize the sum of total_workers, total_days, and total_cost
            return 1 / (1 + total_workers + total_days + total_cost)
    
        # Define the data (replace this with your actual data)
        solution_data = [
            [
                {
                    "id": 8,
                    "solution": {
                    "6": {
                        "[E]targeted_unit_amount": 90,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 1.3333333333333333,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 22.5,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "10": {
                        "[E]targeted_unit_amount": 40.69,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 10.1725,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "14": {
                        "[E]targeted_unit_amount": 22,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 3.3,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "19": {
                        "[E]targeted_unit_amount": 4.1,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 1.282051282051282,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 0.4568571428571428,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "27": {
                        "[E]targeted_unit_amount": 72,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 7.2,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "33": {
                        "[E]targeted_unit_amount": 84,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.6666666666666666,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 126,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "42": {
                        "[E]targeted_unit_amount": 151.92,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4.545454545454546,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 33.422399999999996,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "52": {
                        "[E]targeted_unit_amount": 17.06,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4.545454545454546,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 0.9382999999999998,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "62": {
                        "[E]targeted_unit_amount": 78.72,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3112582781456954,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 23.77344,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "73": {
                        "[E]targeted_unit_amount": 6.81,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 0.34049999999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "79": {
                        "[E]targeted_unit_amount": 12,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 0.5142857142857142,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "84": {
                        "[E]targeted_unit_amount": 12,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.6060606060606061,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 2.1999999999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "95": {
                        "[E]targeted_unit_amount": 12.25,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 8.620689655172413,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 0.23683333333333337,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "103": {
                        "[E]targeted_unit_amount": 219.6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 3.6599999999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "113": {
                        "[E]targeted_unit_amount": 845.99,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 126.8985,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "121": {
                        "[E]targeted_unit_amount": 845.99,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 42.2995,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "128": {
                        "[E]targeted_unit_amount": 159.65,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 8,
                        "[R]total_days_of_working": 0.9978125,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 880000
                    },
                    "137": {
                        "[E]targeted_unit_amount": 662.66,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 16.566499999999998,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "147": {
                        "[E]targeted_unit_amount": 30,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 8,
                        "[R]total_days_of_working": 0.135,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 880000
                    },
                    "155": {
                        "[E]targeted_unit_amount": 15,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 0.108,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "163": {
                        "[E]targeted_unit_amount": 10,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 12.345679012345679,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 0.162,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "171": {
                        "[E]targeted_unit_amount": 2,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 24.390243902439025,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 0.0205,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "184": {
                        "[E]targeted_unit_amount": 1,
                        "[L]unit_defined_price": 140000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.13458950201884254,
                        "[Q]total_of_workers": 8,
                        "[R]total_days_of_working": 0.92875,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1120000
                    },
                    "199": {
                        "[E]targeted_unit_amount": 755.42,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 45.325199999999995,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "207": {
                        "[E]targeted_unit_amount": 755.42,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 7.5542,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "214": {
                        "[E]targeted_unit_amount": 146.14,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 0.8118888888888888,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "223": {
                        "[E]targeted_unit_amount": 599.6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 3.3311111111111114,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "233": {
                        "[E]targeted_unit_amount": 12.25,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 8.620689655172413,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 0.47366666666666674,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "241": {
                        "[E]targeted_unit_amount": 220.78,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 1.577,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "251": {
                        "[E]targeted_unit_amount": 6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 0.108,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
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
                    "6": {
                        "[E]targeted_unit_amount": 90,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 1.3333333333333333,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 13.500000000000002,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "10": {
                        "[E]targeted_unit_amount": 40.69,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 1.6954166666666666,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "14": {
                        "[E]targeted_unit_amount": 22,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 0.9428571428571427,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "19": {
                        "[E]targeted_unit_amount": 4.1,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 1.282051282051282,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 0.35533333333333333,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "27": {
                        "[E]targeted_unit_amount": 72,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 10.799999999999999,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "33": {
                        "[E]targeted_unit_amount": 84,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.6666666666666666,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 42,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "42": {
                        "[E]targeted_unit_amount": 151.92,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4.545454545454546,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 8.355599999999999,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "52": {
                        "[E]targeted_unit_amount": 17.06,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4.545454545454546,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 0.4170222222222221,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "62": {
                        "[E]targeted_unit_amount": 78.72,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3112582781456954,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 11.88672,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "73": {
                        "[E]targeted_unit_amount": 6.81,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 0.2918571428571428,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "79": {
                        "[E]targeted_unit_amount": 12,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 3.5999999999999996,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "84": {
                        "[E]targeted_unit_amount": 12,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.6060606060606061,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 2.1999999999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "95": {
                        "[E]targeted_unit_amount": 12.25,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 8.620689655172413,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 0.35525000000000007,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "103": {
                        "[E]targeted_unit_amount": 219.6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 3.6599999999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "113": {
                        "[E]targeted_unit_amount": 845.99,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 36.25671428571428,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "121": {
                        "[E]targeted_unit_amount": 845.99,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 21.14975,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "128": {
                        "[E]targeted_unit_amount": 159.65,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 1.3304166666666668,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "137": {
                        "[E]targeted_unit_amount": 662.66,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 4.733285714285714,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "147": {
                        "[E]targeted_unit_amount": 30,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 0.18,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "155": {
                        "[E]targeted_unit_amount": 15,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 0.27,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "163": {
                        "[E]targeted_unit_amount": 10,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 12.345679012345679,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 0.135,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "171": {
                        "[E]targeted_unit_amount": 2,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 24.390243902439025,
                        "[Q]total_of_workers": 10,
                        "[R]total_days_of_working": 0.0082,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1100000
                    },
                    "184": {
                        "[E]targeted_unit_amount": 1,
                        "[L]unit_defined_price": 140000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.13458950201884254,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 1.8575,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 560000
                    },
                    "199": {
                        "[E]targeted_unit_amount": 755.42,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 8,
                        "[R]total_days_of_working": 28.328249999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 880000
                    },
                    "207": {
                        "[E]targeted_unit_amount": 755.42,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 7.5542,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "214": {
                        "[E]targeted_unit_amount": 146.14,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 1.0438571428571428,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "223": {
                        "[E]targeted_unit_amount": 599.6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 14.99,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "233": {
                        "[E]targeted_unit_amount": 12.25,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 8.620689655172413,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 0.7105000000000001,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "241": {
                        "[E]targeted_unit_amount": 220.78,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 1.2265555555555556,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "251": {
                        "[E]targeted_unit_amount": 6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 0.216,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
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
                    "6": {
                        "[E]targeted_unit_amount": 90,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 1.3333333333333333,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 7.5,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "10": {
                        "[E]targeted_unit_amount": 40.69,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 10.1725,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "14": {
                        "[E]targeted_unit_amount": 22,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 3.3,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "19": {
                        "[E]targeted_unit_amount": 4.1,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 1.282051282051282,
                        "[Q]total_of_workers": 10,
                        "[R]total_days_of_working": 0.3198,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1100000
                    },
                    "27": {
                        "[E]targeted_unit_amount": 72,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 4.319999999999999,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "33": {
                        "[E]targeted_unit_amount": 84,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.6666666666666666,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 31.5,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "42": {
                        "[E]targeted_unit_amount": 151.92,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4.545454545454546,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 8.355599999999999,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "52": {
                        "[E]targeted_unit_amount": 17.06,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 4.545454545454546,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 1.2510666666666665,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "62": {
                        "[E]targeted_unit_amount": 78.72,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3112582781456954,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 2.6414933333333335,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "73": {
                        "[E]targeted_unit_amount": 6.81,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 2.0429999999999997,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "79": {
                        "[E]targeted_unit_amount": 12,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 10,
                        "[R]total_days_of_working": 0.36,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1100000
                    },
                    "84": {
                        "[E]targeted_unit_amount": 12,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.6060606060606061,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 2.8285714285714287,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "95": {
                        "[E]targeted_unit_amount": 12.25,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 8.620689655172413,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 0.7105000000000001,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "103": {
                        "[E]targeted_unit_amount": 219.6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 10,
                        "[R]total_days_of_working": 1.0979999999999999,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1100000
                    },
                    "113": {
                        "[E]targeted_unit_amount": 845.99,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 84.599,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
                    "121": {
                        "[E]targeted_unit_amount": 845.99,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 42.2995,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "128": {
                        "[E]targeted_unit_amount": 159.65,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 10,
                        "[R]total_days_of_working": 0.79825,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1100000
                    },
                    "137": {
                        "[E]targeted_unit_amount": 662.66,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 4.733285714285714,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "147": {
                        "[E]targeted_unit_amount": 30,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 7,
                        "[R]total_days_of_working": 0.15428571428571428,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 770000
                    },
                    "155": {
                        "[E]targeted_unit_amount": 15,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 8,
                        "[R]total_days_of_working": 0.0675,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 880000
                    },
                    "163": {
                        "[E]targeted_unit_amount": 10,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 12.345679012345679,
                        "[Q]total_of_workers": 10,
                        "[R]total_days_of_working": 0.081,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 1100000
                    },
                    "171": {
                        "[E]targeted_unit_amount": 2,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 24.390243902439025,
                        "[Q]total_of_workers": 5,
                        "[R]total_days_of_working": 0.0164,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 550000
                    },
                    "184": {
                        "[E]targeted_unit_amount": 1,
                        "[L]unit_defined_price": 140000,
                        "[O]capability_of_one_day_work_per_one_worker": 0.13458950201884254,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 2.4766666666666666,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 420000
                    },
                    "199": {
                        "[E]targeted_unit_amount": 755.42,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 3.3333333333333335,
                        "[Q]total_of_workers": 9,
                        "[R]total_days_of_working": 25.180666666666664,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 990000
                    },
                    "207": {
                        "[E]targeted_unit_amount": 755.42,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 1,
                        "[R]total_days_of_working": 37.771,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 110000
                    },
                    "214": {
                        "[E]targeted_unit_amount": 146.14,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 1.8267499999999999,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "223": {
                        "[E]targeted_unit_amount": 599.6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 6,
                        "[R]total_days_of_working": 4.996666666666667,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 660000
                    },
                    "233": {
                        "[E]targeted_unit_amount": 12.25,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 8.620689655172413,
                        "[Q]total_of_workers": 4,
                        "[R]total_days_of_working": 0.35525000000000007,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 440000
                    },
                    "241": {
                        "[E]targeted_unit_amount": 220.78,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 20,
                        "[Q]total_of_workers": 2,
                        "[R]total_days_of_working": 5.5195,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 220000
                    },
                    "251": {
                        "[E]targeted_unit_amount": 6,
                        "[L]unit_defined_price": 110000,
                        "[O]capability_of_one_day_work_per_one_worker": 27.77777777777778,
                        "[Q]total_of_workers": 3,
                        "[R]total_days_of_working": 0.072,
                        "[T]total_cost_by_unit_defined_price_and_total_of_workers": 330000
                    },
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
        ]

        # Create an instance of the PyGAD optimizer
        ga = pygad.GA(num_generations=100,
              num_parents_mating=10,
              fitness_func=fitness_function,
              sol_per_pop=20)

        # Start the optimization process
        ga.run()

        # Get the best solution and its fitness value
        best_solution, best_fitness = ga.output_dict['last_generation']['solution'], ga.output_dict['last_generation']['fitness']
        
        # Print the best solution and its fitness
        print("Best Solution:", best_solution)
        print("Best Fitness:", best_fitness)
