import re
import ast
import random as rnd


class Utils:
    '''
    Итилиты для rnd_In
    '''

    @staticmethod
    def is_correct_file_name(file_name: str) -> bool:
        '''
        Метод проверяет соответстиве формату файла
        :param file_name: строка с именем файла
        :return: флаг согнализирующий о корректности имени файла
        '''
        if re.match(r"(^[a-zA-Z0-9_.+-]+\.txt$)", file_name):
            return True
        return False

    @staticmethod
    def is_correct_line_with_type_of_transport(line: str) -> bool:
        '''
        Проверяет корректность числа описывающего тип ТС
        :param line: строка с числом
        :return: флаг согнализирующий о корректности типа ТС
        '''
        # Check: is only one number in line
        if len(line.split()) != 1:
            return False
        # Check: is the number in the range 0 to 2
        if 0 > int(line.split()[0]) < 2:
            return False
        # if the program reaches here then the format is correct
        return True

    @staticmethod
    def is_correct_line_with_parameters_of_transport(line: str) -> bool:
        '''
        Метод проверяет корректность ввода параметром ТС
        :param line: строка с параметрами
        :return: флаг согнализирующий о корректности параметров
        '''
        # Check: are three parameters
        if len(line.split()) != 3:
            return False
        # Check: are numbers integer
        # TODO: Проверить что выводит ast.literal_eval(line.split()[0]
        print(ast.literal_eval(line.split()[0]))
        if (ast.literal_eval(line.split()[0]) != "!!!!!!!!!!!!"
                or ast.literal_eval(line.split()[0]) != "!!!!!!!!!!"
                or ast.literal_eval(line.split()[0]) != "!!!!!!!"):
            # return False
            pass
        return True

    @staticmethod
    def generate_random_value(minimum: int, maximum: int) -> int:
        '''
        Генератор числа
        :param minimum: нижняя граница
        :param maximum: верхняя граница
        :return: случайное число
        '''
        return rnd.randint(minimum, maximum)

    @staticmethod
    def read_number(line: str):
        '''
        Проверяет число на число))
        :param line: строка
        :return: None - если не удалось спарсиьт; Число - если удалось спарсить
        '''
        try:
            output = int(line)
            return output
        except ValueError:
            print(f"Couldn't read this number: {line}")
        return None


