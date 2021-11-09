# coding=utf-8
from abc import abstractmethod

from typing import TextIO

class Transport(object):
    '''
    Абстрактный класс для типов ТС
    '''
    def __init__(self, fuel_tank_capacity: int, fuel_consumption: int):
        self.fuel_tank_capacity = fuel_tank_capacity
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return ""

    @abstractmethod
    def rnd_In(self) -> None:
        '''
        Создание объекта со случайными параметрами
        :return:
        '''

    @abstractmethod
    def In(self, file: TextIO) -> None:
        '''
        Чтение из файла данных объекта и создание его
        '''

    @abstractmethod
    def max_distance(self) -> int:
        '''
        Вычисляет максимальное растояние для автомобиля
        '''

    @abstractmethod
    def parameters(self) -> str:
        '''
        Объект для генериации входных файлов
        '''


