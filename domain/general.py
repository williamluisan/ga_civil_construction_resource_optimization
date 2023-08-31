class General:
    """
    This class is to handle the general domain of civil engineering calculation
    """

    def get_capability_of_one_worker_to_complete_in_one_day_compare_to_targeted_unit(OH_coefficient: float, unit: str = None) -> (float, str):
        """
        Args:
            OH_coefficient (int): OH = Orang Hari (OH)
            unit (int)

        Returns:
            int: the total of workday and the corresponding unit
        """
        total_of_workday = 1 / OH_coefficient
        return total_of_workday, unit

    def get_total_days_to_work_by_total_workers_compare_to_targeted_units(capability_of_one_day_work_per_one_worker: float, total_of_worker: int, targeted_unit_amount: float) -> float:
        result = targeted_unit_amount / (capability_of_one_day_work_per_one_worker * total_of_worker)
        return result
    
    def get_total_cost_by_unit_defined_price_and_total_of_workers(unit_defined_price: float, total_of_workers: int) -> float:
        result = unit_defined_price * total_of_workers
        return result