import utilsIn
import random
import languages
import enum


# -----------------------------------------------
class Legacy(enum.Enum):
    SINGLE = 1
    MULTIPLE = 2
    INTERFACE = 3
    ERROR = 4


# ----------------------------------------------
class ObjectOriented(languages.Languages):
    def __init__(self):
        """
            Инициализация
            :argument self.name: название языка
            :argument self.year: год
            :argument self.popularity: действительное число популярность
            :argument self.has_abstract_variables: название языка
            :argument self.legacy: enum class
        """
        self.name = ""
        self.year = 0
        self.popularity = 0.0
        self.has_abstract_variables = False
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
        self.has_abstract_variables = bool(str_line_array[i + 3])
        self.legacy = Legacy(str_line_array[i + 4])
        i += 5
        return i

    def read_rnd(self):
        """
            Инициализация случайными буквами и цифрами
        """
        self.name = utilsIn.rndString(10)
        self.year = random.randrange(1945, 2021)
        self.popularity = random.uniform(1, 99)
        self.has_abstract_variables = random.randrange(0, 2) == 0
        self.legacy = Legacy(random.randrange(1, 3))

    def print(self):
        """
            Вывод информации
        """
        print("[ObjectOriented]: name = ", self.name, " year = ", self.year, " popularity = ",
              round(self.popularity, 2),
              " abstract variables = ", self.has_abstract_variables, " legacy = ", self.legacy.name, "quotient = ",
              round(self.quotient(), 2))
        pass

    def write(self, stream):
        """
            Запись информации в поток
            :param stream: поток
        """
        stream.write(
            "[ObjectOriented]: name = {}  year = {}  popularity = {} abstract variables = {} legacy = {}, quotient = {}".format \
                (self.name, self.year, round(self.popularity, 2), self.has_abstract_variables, self.legacy,
                 round(self.quotient(), 2)))
        pass

    def quotient(self):
        """
        Вычисление деления int year на длину name
        :return: float result
        """
        return float(self.year) / float(len(self.name))
