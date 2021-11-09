from typing import TextIO
import time

from utils import Utils
from transport.transport import Transport
from transport.bus import Bus
from transport.car import Car
from transport.truck import Truck


class Container(object):
    '''
    Класс описывающий список объектов унаследованных от transport
    '''
    def __init__(self):
        self.cont = []

    def __del__(self):
        for i in self.cont:
            del i
        del self.cont

    @staticmethod
    def In(file: TextIO):
        '''
        Метод заполняет контейнер из файла
        :param file:
        :return:
        '''
        container = Container()

        count_of_elements = Utils.read_number(file.readline())
        if count_of_elements is None or count_of_elements <= 0:
            raise ValueError("Incorrect number of elements in the file")

        for i in range(count_of_elements):
            transport_type = Utils.read_number(file.readline())
            print(transport_type)
            if transport_type is None:
                raise Exception()
            if transport_type == 0:
                car = Car(0, 0, 0)
                car.In(file)
                container.cont.append(car)
            if transport_type == 1:
                bus = Bus(0, 0, 0)
                bus.In(file)
                container.cont.append(bus)
            if transport_type == 2:
                truck = Truck(0, 0, 0)
                truck.In(file)
                container.cont.append(truck)

            #container.cont.append(transport_type)
        return container

    @staticmethod
    def rnd_In(count_of_elements: int):
        '''
        Метод заполняет контейнер случайными объектыми
        '''
        container = Container()
        for i in range(count_of_elements):
            transport = Transport(0, 0)
            container.cont.append(transport.rnd_In())
        return container

    def out(self, file: TextIO):
        file.write(f'Count of elements - {len(self.cont)}\n')
        for i in range(len(self.cont)):
            file.write(str(self.cont[i]))

        start = time.time()
        self.cont = sort(self.cont)
        end = time.time()
        print(f"Time: {end - start :0.09f} sec")

        file.write("Sorted\n")
        for i in range(len(self.cont)):
            file.write(str(self.cont[i]))


    def create_file(self, file_name: str):
        with open(file_name, 'w') as file:
            for obj in self.cont:
                file.write(obj.parameters())


def sort(array):
    '''
    Метод сортирует контейнер
    :param array: текущий контейнер
    '''
    if len(array) == 1 or len(array) == 0:
        return array
    l = array[:len(array) // 2]
    r = array[len(array) // 2:]
    sort(l)
    sort(r)
    k = 0
    n = 0
    m = 0
    c = [0] * (len(l) + len(r))
    while n < len(l) and m < len(r):
        if l[n].max_distance() < r[m].max_distance():
            c[k] = l[n]
            n += 1
        else:
            c[k] = r[m]
            m += 1
        k += 1
    while n < len(l):
        c[k] = l[n]
        n += 1
        k += 1
    while m < len(r):
        c[k] = r[m]
        m += 1
        k += 1
    for i in range(len(array)):
        array[i] = c[i]
    return array
