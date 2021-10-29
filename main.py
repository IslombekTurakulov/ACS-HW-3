import sys
import time

# ----------------------------------------------
from container import Container
from utilsIn import inLines

if __name__ == '__main__':
    start_time = time.time()
    print(len(sys.argv), sys.argv)
    if len(sys.argv) != 5:
        print("incorrect command line!\n"
              "  Waited:\n"
              "     command -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     command -n number outfile01 outfile02\n")
        exit()
    print('==> Start')
    # Создаём контейнер
    container = Container()

    if sys.argv[1] == "-f":
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        inputFile = sys.argv[2]
        try:
            infile = open(inputFile)
        except IOError:
            # Если файл не существует, мы создаём его.
            infile = open(inputFile, 'w')
        # Чтение файла (открытие потока)
        inputLine = infile.read()
        # Закрытие потока
        infile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = inputLine.replace("\n", " ").split(" ")
        figNum = inLines(container, strArray)
        # container.print()
        # Открытие потока для записи в первый файл объектов
        outfile = open(sys.argv[3], 'w+')
        container.write(outfile)
        outfile.close()
        # Вывод времени записи
        print("Source: ",
              round(time.time() - start_time, 5), " seconds")
        # Открытие потока для записи во второй файл отсортированных объектов
        outfileSecond = open(sys.argv[4], 'w+')
        container.sort()
        container.write(outfileSecond)
        outfileSecond.close()
        # Вывод времени записи
        print("Sorted: ",
              round(time.time() - start_time, 5), " seconds")
    elif sys.argv[1] == "-n":
        # Парсим третий аргумент массива
        length = int(sys.argv[2])
        # Проверка на размерность
        if length < 1 or length > 10000:
            print("incorrect number of languages = {}. Set 0 < number <= 10000\n", length)
            exit()
        # Функция рандомизации
        container.staticRndIn(length)
        # container.print()
        outfile = open(sys.argv[3], 'w+')
        container.write(outfile)
        outfile.close()
        # Вывод времени
        print("Source: ",
              round(time.time() - start_time, 5), " seconds")
        outfileSecond = open(sys.argv[4], 'w+')
        container.sort()
        container.write(outfileSecond)
        # Вывод времени
        print("Sorted: ",
              round(time.time() - start_time, 5), " seconds")
        outfileSecond.close()
    else:
        print("incorrect qualifier value!\n"
              "  Waited:\n"
              "     command -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     command -n number outfile01 outfile02\n");
        exit()
    print('==> Finish')
