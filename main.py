import os
import sys
import time
from pycallgraph import PyCallGraph, Config
from pycallgraph.output import GraphvizOutput
from container import Container
from utilsIn import inLines

if __name__ == '__main__':
    os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
    config = Config(max_depth=100)
    graphviz = GraphvizOutput(output_file='./reports/procedural_memory.png')
    with PyCallGraph(output=graphviz, config=config):
        start_time = time.time()
        print("Length: ", len(sys.argv), "\nIn: ", sys.argv)
        if len(sys.argv) != 5:
            print("Incorrect command line!\n"
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
            length = int(sys.argv[2])
            # Проверка на размерность
            if length < 1 or length > 10000:
                print("Incorrect number of languages = {}. Set 0 < number <= 10000\n", length)
                exit()
            # Функция рандомизации
            container.staticRndIn(length)
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
            print("Incorrect qualifier value!\n"
                  "  Waited:\n"
                  "     command -f <infile> <outfile01> <outfile02>\n"
                  "  Or:\n"
                  "     command -n <number> <outfile01> <outfile02>\n");
            exit()
    print('==> Finish')
