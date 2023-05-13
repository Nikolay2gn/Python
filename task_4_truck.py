# Реализуйте класс Truck (грузовик). Грузовик может перевозить посылки - Box из предыдущего задания
#     Импортиуйте модуль task_3_box из предыдущего задания.
#     Создайте несколько экземпляров класса Box.
#     Проверьте работу методов класса Box
#     Создайте класс Truck (грузовик), который будет иметь несколько атрибутов, присущих грузовику.
#     Реализуйте атрибут capacity (емкость), в котором будет реализовано хранилище посылок (Box): [box1, box2 ...]
#     Переопределите методы __str__, __add__, __sub__ для реализации отображения грузовика, загрузки и выгрузки посылок.
#     Продемонстрируйте работу класса Truck.

from task_3_box import Box
from random import randint
rand = randint(10, 100000000)
box1 = Box(rand, 'Computer', 'Kazan', 'Moscow')
box2 = Box(rand, 'Notepad', 'Moscow', 'Volzhsk')
box3 = Box(rand, 'Food', 'Uralsk', 'Novgorod')
print(box1.postcode)
print(box1.name)
print(box1.from_city)
print(box1.target_city)
box1.target_city_change = 'Paris'
print(box1.target_city)
print('------------')
print(box2.postcode)
print(box2.name)
print(box2.from_city)
print(box2.target_city)
box2.target_city_change = 'Ufa'
print(box2.target_city)

class Truck:
    def __init__(self,name,weight,max_speed,length,width,capacity=[]):
        self.name = name
        self.weight = weight
        self.max_speed = max_speed
        self.length = length
        self.width = width
        self.capacity = capacity

    def __str__(self):
        return f'Truck(capacity={len(self.capacity)})'

    def __add__(self, box):
        self.capacity.append(box)
        return self

    def __sub__(self, box):
        if len(self.capacity) > 0:
            self.capacity.remove(box)
            return self

truck1 = Truck('ZIL',1000,333,5,2)
truck1+=box1
truck1+=box2
print(truck1)
truck1+=box3
print(truck1)
truck1-=box3
print(truck1)




