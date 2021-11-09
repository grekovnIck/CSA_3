from abc import ABC
from typing import TextIO

from utils import Utils
from transport.transport import Transport


class Truck(Transport, ABC):
    '''
    Класс описывает грузовик
    '''

    def __init__(self, fuel_tank_capacity: int, fuel_consumption: int, lifting_capacity: int):
        super().__init__(fuel_tank_capacity, fuel_consumption)
        self.lifting_capacity = lifting_capacity

    def In(self, file: TextIO) -> bool:
        '''
        Метод для чтения из файла
        :param file: дескриптор файла, открытый только на чтение
        :return: флаг сигнализирующий об успешности чтения чисел из файла.
        '''
        line = file.readline()
        try:
            print(int(line.split()[2]))
            if not Utils.is_correct_line_with_parameters_of_transport(line):
                if not Utils.is_correct_line_with_parameters_of_transport(line):
                    print('Incorrect truck parameters!')
                    return False
            self.fuel_tank_capacity = int(line.split()[0])
            self.fuel_consumption = int(line.split()[1])
            self.max_speed = int(line.split()[2])
            return True
        except ValueError:
            print(f"Can't parse the line: {line}")
        except Exception as ex:
            print(ex)
        return False

    def rnd_In(self) -> None:
        '''
        Случайное заполение объекта
        '''
        min_value = 1
        max_value = 1000
        #self.fuel_tank_capacity = Utils.generate_random_value(min_value, max_value)
        #self.fuel_consumption = Utils.generate_random_value(min_value, max_value)
        self.lifting_capacity = Utils.generate_random_value(min_value, max_value)

    def parameters(self) -> str:
        data = f"2\n{self.fuel_tank_capacity} {self.fuel_consumption} {self.lifting_capacity}\n"
        return data

    def __str__(self):
        return f"Truck: fuel tank capacity: {self.fuel_tank_capacity}; fuel consumption: {self.fuel_consumption}; " \
               f"lifting capacity: {self.lifting_capacity}; max distance: {self.max_distance()}\n"

    def max_distance(self) -> int:
        if self.fuel_consumption == 0:
            return 0
        return int(self.fuel_tank_capacity / self.fuel_consumption)
