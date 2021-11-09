# coding=utf-8
import time
from container.container import Container
from utils import Utils
import sys

INFO = '''
Задание №3 по Архитектуре вычислительных систем
Выполин Греков Николай, БПИ204
'''

DESCRIPTION = '''
В программе реализован слудующий функционал:
\t1. Создание файла со случайнами входными данными;
\tПример: -rnd <кол-во объектов> <имя файла>.txt
\t2. Чтение и обработка данных из файла, и далее запис их в файл
\tПример: -w <имя файла для чтения>.txt <имя файла для записи>.txt
'''

HELP = '''
В первой строке файла должно стоять число - кол-во объектов;
Далее с новой строки вводятся данные об объектах:
<Тип автомобиля> - Car - 0; Bus - 1; Truck - 2.
<Запас топлива> <Расход топлива> <Доп данные об транспорте>
'''


def check_file_name(file_name: str) -> bool:
    '''
    Проверяет корректность названия файла
    :param file_name: название файла
    :return: булево значение
    '''
    if not Utils.is_correct_file_name(file_name):
        print(DESCRIPTION)
        return False
    return True


def is_number(line: str) -> bool:
    '''
    Проверяет является ли строка числом
    :param line: строка с числом
    :return: булево значение
    '''
    try:
        if int(line) < 0:
            print("Incorrect number! Number can't be less then zero")
            return False
        return True
    except Exception:
        print("Incorrect count of elements")


# Check correctness of the file name
def main(argv):
    if 2 < len(argv) > 4:
        print(DESCRIPTION)
        return
    if argv[1] == "-rnd":
        if is_number(argv[2]) and check_file_name(argv[3]):
            return
        container = Container.rnd_In(int(argv[2]))
        try:
            container.out(argv[3])
            del container
        except Exception as ex:
            del container
            print(ex)
    if argv[1] == "-w":
        if not check_file_name(argv[2]) and not check_file_name(argv[3]):
            return
        try:
            file_input = open(argv[2], 'r')
            container = Container.In(file_input)
            file_input.close()
            print("Values was read")
            file_output = open(argv[3], 'w')
            container.out(file_output)
            file_output.close()
            del container
        except Exception as ex:
            print(ex)
            return
    if argv[1] == "-c":
        container = Container.rnd_In(int(argv[2]))
        container.create_file(argv[3])


if __name__ == '__main__':
    main(sys.argv)
