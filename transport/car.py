# coding=utf-8
from abc import ABC
from typing import TextIO

from utils import Utils
from transport.transport import Transport


class Car(Transport, ABC):
    '''
    Класс описывает легковой автомобиль
    '''
    def __init__(self, fuel_tank_capacity: int, fuel_consumption: int, max_speed: int):
        #super().__init__(fuel_tank_capacity, fuel_consumption)
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed

    def In(self, file: TextIO) -> bool:
        '''
        Метод для чтения из файла
        :param file: дескриптор файла, открытый только на чтение
        :return: флаг сигнализирующий об успешности чтения чисел из файла.
        '''
        line = file.readline()
        try:
            if not Utils.is_correct_line_with_parameters_of_transport(line):
                if not Utils.is_correct_line_with_parameters_of_transport(line):
                    print('Incorrect bus parameters!')
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
        self.max_speed = Utils.generate_random_value(min_value, max_value)

    def parameters(self) -> str:
        data = f"0\n{self.fuel_tank_capacity} {self.fuel_consumption} {self.max_speed}\n"
        return data

    def __str__(self):
        return f"Car:   fuel tank capacity: {self.fuel_tank_capacity}; fuel consumption: {self.fuel_consumption}; " \
               f"max speed: {self.max_speed}; max distance: {self.max_distance()}\n"

    def max_distance(self) -> int:
        if self.fuel_consumption == 0:
            return 0
        return int(self.fuel_tank_capacity / self.fuel_consumption)
