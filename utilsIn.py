import random
import string

from functional import Functional
from objectOriented import ObjectOriented
from procedural import Procedural


def inLines(container, str_array):
    """
    :param container: Contains objects
    :param str_array: Input
    :return: string
    """
    array_len = len(str_array)
    i = 0  # Индекс, задающий текущую строку в массиве
    count = 0
    while i < array_len:
        line = str_array[i]
        key = int(line)
        if key == 1:
            i += 1
            shape = Functional()
            i = shape.read_in(str_array, i)
        elif key == 2:
            i += 1
            shape = ObjectOriented()
            i = shape.read_in(str_array, i)
        elif key == 3:
            i += 1
            shape = Procedural()
            i = shape.read_in(str_array, i)
        else:
            return count
        if i == 0:
            return count
        count += 1
        container.store.append(shape)
    return count


def inRnd():
    """
    Выбор случайного сгенерированного объекта
    :return: Объект базового класса Language
    """
    key = random.randrange(1, 4)
    if key == 1:  # признак функциональности
        language = Functional()
        language.read_rnd()  # рандомизация функционального языка с возвратом позиции за ним
        return language
    elif key == 2:  # признак ооп
        language = ObjectOriented()
        language.read_rnd()  # чтение ооп языка с возвратом позиции за ним
        return language
    else:
        language = Procedural()
        language.read_rnd()  # чтение процедурного языка с возвратом позиции за ним
        return language


def rndString(length_str):
    """
    Рандомизация случайных букв
    :param length_str: длина строки
    :return: случайная строка
    """
    letters = string.ascii_uppercase + string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length_str))
    return result
