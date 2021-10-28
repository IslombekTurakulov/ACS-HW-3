import utilsIn
import random
import languages
from enum import Enum


# -----------------------------------------------
class Legacy(Enum):
    SINGLE = 1
    MULTIPLE = 2
    INTERFACE = 3
    ERROR = 4


# ----------------------------------------------
class ObjectOriented(languages.Languages):
    def __init__(self):
        self.name = ""
        self.year = 0
        self.popularity = 0.0
        self.has_abstract_variables = False
        self.legacy = Legacy

    def read_line(self, str_line_array, i):
        # должно быть как минимум четыре непрочитанных значения в массиве
        if i >= len(str_line_array) - 4:
            return 0
        self.name = str_line_array[i]
        self.year = int(str_line_array[i + 1])
        self.popularity = float(str_line_array[i + 2])
        self.has_abstract_variables = bool(str_line_array[i + 3])
        self.legacy = Legacy(str_line_array[i + 4])
        i += 5
        return i

    def read_rnd(self):
        self.name = utilsIn.rndString(10)
        self.year = random.randrange(1945, 2021)
        self.popularity = random.uniform(1, 99)
        self.has_abstract_variables = random.randrange(0, 2) == 0
        self.legacy = Legacy(random.randrange(1, 3))

    def print(self):
        print("[ObjectOriented]: name = ", self.name, " year = ", self.year, " popularity = ", round(self.popularity, 2),
              " abstract variables = ", self.has_abstract_variables, " legacy = ", self.legacy, "quotient = ", round(self.quotient(), 2))
        pass

    def write(self, stream):
        stream.write(
            "[ObjectOriented]: name = {}  year = {}  popularity = {} abstract variables = {} legacy = {}, quotient = {}".format \
                (self.name, self.year, round(self.popularity, 2), self.has_abstract_variables, self.legacy, round(self.quotient(), 2)))
        pass

    def quotient(self):
        return float(self.year) / len(self.name)
        pass
