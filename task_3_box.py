# Создайте класс Box (посылка), у которого будет приватные атрибуты:
#     postcode (номер отправления),
#     name (имя отправителя),
#     from_city (город отправителя),
#     target_city (город назначения).
#     Реализуйте методы, которые будут давать возможность доступа к приватным атрибутам.
#     Реализуйте метод, который будет давать возможность менять город назанчения
#     Назовите модуль task_3_box и сохраните его

from random import randint
class Box:
    def __init__(self, postcode, name, from_city, target_city):
        self.__postcode = postcode
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    @property
    def postcode(self):
        return self.__postcode

    @property
    def name(self):
        return self.__name

    @property
    def from_city(self):
        return self.__from_city

    @property
    def target_city(self):
        return self.__target_city

    @target_city.setter
    def target_city_change(self, new_city):
        self.__target_city = new_city
        return self.__target_city


# rand = randint(10, 100000000)
# ex1 = Box(rand, 'Computer', 'Kazan', 'Moscow')
# print(ex1.postcode)
# print(ex1.name)
# print(ex1.from_city)
# print(ex1.target_city)
# ex1.target_city_change = 'Ufa'
# print(ex1.target_city)














