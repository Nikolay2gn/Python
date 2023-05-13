# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта - одежда (Cloth), которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто Coat) и рост (для костюма Suit).
# Это могут быть обычные числа V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#     для пальто V/6.5+0.5
#     для костюма 2H+0.3 Проверить работу этих методов на реальных данных.
# Выполнить общий подсчет расхода ткани, который пойдет на пошив всех костюмов и всех пальто соответственно.
# Реализовать абстрактыне классы для основных классов проекта и проверить работу декоратора @property.
# Подсказка:
#     Воспользуйтесь абстрактным классом при создании класса Cloth
#     Определите абстрактные методы подсчета количества ткани
#     Количество ткани reserved сделайте атрибутом класса ( определяется вне конструктора)

from abc import ABC, abstractmethod
class Cloth:
    def total_reserved(self):
        return self.reserved() * self.quantity

    @abstractmethod
    def reserved(self):
        pass


class Coat(Cloth):
    def __init__(self, name, size, quantity=1):
        self.name = name
        self.__size = size
        self.quantity = quantity

    def reserved(self):
        return (self.size / 6.5) + 0.5

    @property
    def size(self):
        return self.__size


class Suit(Cloth):
    def __init__(self, name, height, quantity=1):
        self.name = name
        self.__height = height
        self.quantity = quantity

    def reserved(self):
        return (2 * self.height) + 0.3

    @property
    def height(self):
        return self.__height


coat = Coat('Пальто', 150, 4)
suit = Suit('Костюм тройка', 190)
print(coat.size)
print(coat.total_reserved())
print(suit.height)
print(suit.total_reserved())

