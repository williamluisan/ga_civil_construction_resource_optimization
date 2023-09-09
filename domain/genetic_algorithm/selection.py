import helpers.general as h_general
import json
from collections import OrderedDict

class Selection:
    def __init__(self, data: dict):
        self.data = data

    def sort_by_efficiency_value(self, sort: str="asc"):
        data = self.data
        sorted_data = sorted(data, key=lambda x: x['efficiency_value'])

        return sorted_data