import utilsIn
from random import *
from languages import *
from enum import Enum


# -----------------------------------------------
class Legacy(Enum):
    DYNAMIC = 1
    STRICT = 2
    ERROR = 3


# ----------------------------------------------
class Functional(Languages):
    def __init__(self):
        self.name = ""
        self.year = 0
        self.popularity = 0.0
        self.lazy_calculation = False
        self.legacy = Legacy

    def read_line(self, str_line_array, i):
        # должно быть как минимум четыре непрочитанных значения в массиве
        if i >= len(str_line_array) - 4:
            return 0
        self.name = str_line_array[i]
        self.year = int(str_line_array[i + 1])
        self.popularity = float(str_line_array[i + 2])
        self.lazy_calculation = bool(str_line_array[i + 3])
        self.legacy = Legacy(int(str_line_array[i + 4]))
        i += 5
        return i

    def read_rnd(self):
        self.name = utilsIn.rndString(10)
        self.year = randrange(1945, 2021)
        self.popularity = uniform(1, 99)
        self.lazy_calculation = randrange(0, 2) == 0
        self.legacy = Legacy(randrange(1, 3))

    def print(self):
        print("[Functional]: name = ", self.name, " year = ", self.year, " popularity = ", round(self.popularity, 2),
              " lazy calculation = ", self.lazy_calculation, " legacy = ", self.legacy.name, "quotient = ",
              round(self.quotient(), 2))
        pass

    def write(self, stream):
        stream.write(
            "[Functional]: name = {}  year = {}  popularity = {} lazy calculation = {} legacy = {}, quotient = {}".format \
                (self.name, self.year, round(self.popularity, 2), self.lazy_calculation, self.legacy.name,
                 round(self.quotient(), 2)))
        pass

    def quotient(self):
        return float(self.year) / len(self.name)
        pass
