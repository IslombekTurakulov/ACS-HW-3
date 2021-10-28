from random import *
import utilsIn
from languages import *


# ----------------------------------------------
class Procedural(Languages):
    def __init__(self):
        self.name = ""
        self.year = 0
        self.popularity = 0.0
        self.has_abstract_variables = False

    def read_line(self, str_line_array, i):
        # должно быть как минимум четыре непрочитанных значения в массиве
        if i >= len(str_line_array) - 3:
            return 0
        self.name = str_line_array[i]
        self.year = int(str_line_array[i + 1])
        self.popularity = float(str_line_array[i + 2])
        self.has_abstract_variables = bool(str_line_array[i + 3])
        i += 4
        return i

    def read_rnd(self):
        self.name = utilsIn.rndString(10)
        self.year = randrange(1945, 2021)
        self.popularity = uniform(1, 99)
        self.has_abstract_variables = randrange(0, 2) == 0

    def print(self):
        print("[Procedural]: name = ", self.name, " year = ", self.year, " popularity = ", round(self.popularity, 2),
              " abstract variables = ", self.has_abstract_variables, ", quotient = ",
              round(self.quotient(), 2))
        pass

    def write(self, stream):
        stream.write(
            "[Procedural]: name = {}  year = {}  popularity = {} abstract variables = {}, quotient = {}".format \
                (self.name, self.year, round(self.popularity, 2), self.has_abstract_variables,
                 round(self.quotient(), 2)))
        pass

    def quotient(self):
        return float(self.year) / len(self.name)
        pass
