import utilsIn
import random
import languages
import enum


# -----------------------------------------------
class Legacy(enum.Enum):
    DYNAMIC = 1
    STRICT = 2
    ERROR = 3


# ----------------------------------------------
class Functional(languages.Languages):
    def __init__(self):
        """
         Инициализация
        :argument self.name: название языка
        :argument self.year: год
        :argument self.popularity: действительное число популярность
        :argument self.lazy_calculation: название языка
        """
        self.name = ""
        self.year = 0
        self.popularity = 0.0
        self.lazy_calculation = False
        self.legacy = Legacy

    def read_line(self, str_line_array, i):
        """
        Чтение строки
        :param str_line_array: массив строк
        :param i: количество значений
        :return: int i
        """
        # должно быть как минимум четыре непрочитанных значения в массиве
        if i >= len(str_line_array) - 4:
            return 0
        self.name = str_line_array[i]
        self.year = int(str_line_array[i + 1])
        self.popularity = float(str_line_array[i + 2])
        self.lazy_calculation = int(str_line_array[i + 3]) == 0
        self.legacy = Legacy(int(str_line_array[i + 4]))
        i += 5
        return i

    def read_rnd(self):
        """
        Инициализация случайными буквами и цифрами
        """
        self.name = utilsIn.rndString(10)
        self.year = random.randrange(1945, 2021)
        self.popularity = random.uniform(1, 99)
        self.lazy_calculation = random.randrange(0, 2) == 0
        self.legacy = Legacy(random.randrange(1, 4))

    def print(self):
        """
        Вывод информации
        """
        print("[Functional]: name = ", self.name, " year = ", self.year, " popularity = ", round(self.popularity, 2),
              " lazy calculation = ", self.lazy_calculation, " legacy = ", self.legacy.name, "quotient = ",
              round(self.quotient(), 2))
        pass

    def write(self, stream):
        """
        Запись информации в поток
        :param stream: поток
        """
        stream.write(
            "[Functional]: name = {}  year = {}  popularity = {} lazy calculation = {} legacy = {}, quotient = {}".format \
                (self.name, self.year, round(self.popularity, 2), self.lazy_calculation, self.legacy.name,
                 round(self.quotient(), 2)))
        pass

    def quotient(self):
        """
        Вычисление деления int year на длину name
        :return: float result
        """
        return float(self.year) / float(len(self.name))
