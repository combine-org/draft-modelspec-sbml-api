import re

class SId(str):
    def __new__(cls, string):
        'enforce restrictions'

        if not re.fullmatch('[_A-Za-z][_A-Za-z0-9]*',string):
            raise Exception('invalid SId',string)

        return super().__new__(cls, string)
