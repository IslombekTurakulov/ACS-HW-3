import random
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
    fig_num = 0
    while i < array_len:
        str = str_array[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)
        if key == 1:  # признак прямоугольника
            i += 1
            shape = Functional()
            i = shape.read_line(str_array, i)  # чтение функционального языка с возвратом позиции за ним
        elif key == 2:  # признак треугольника
            i += 1
            shape = ObjectOriented()
            i = shape.read_line(str_array, i)  # чтение ооп языка с возвратом позиции за ним
        elif key == 3:
            i += 1
            shape = Procedural()
            i = shape.read_line(str_array, i)
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return fig_num
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return fig_num
        fig_num += 1
        container.store.append(shape)
    return fig_num


def inRnd():
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
    result = ""
    letters = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
        "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c",
        "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    while i < length_str:
        result += letters[random.randrange(1, 60)]
        i += 1
    return result
