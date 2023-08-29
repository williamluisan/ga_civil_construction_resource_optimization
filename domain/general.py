class General:
    """
    This class is to handle the general domain of civil engineering calculation
    """

    def get_total_of_workday_compare_to_targeted_unit(OH_coefficient: float, unit: str = None) -> (float, str):
        """
        Args:
            OH_coefficient (int): OH = Orang Hari (OH)
            unit (int)

        Returns:
            int: the total of workday and the corresponding unit
        """
        total_of_workday = 1 / OH_coefficient
        return total_of_workday, unit

