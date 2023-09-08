import helpers.general as h_general

class Selection:
    def __init__(self, data: dict):
        self.data = data

    def sort_by_efficiency_value(self, sort: str="asc"):
        data = self.data

        print(data.items())