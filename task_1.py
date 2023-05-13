# Сооздайте класс Person с приватными атрибутами name, age, surname.
# Реализуйте методы name, age, surname, которые будут давать доступ к аналогичным приватным атрибутам.
# Создайте сеттер, который будет давать возможность поменять атрибут age.
class Person:
    def __init__(self, name, age, surname):
        self.__name = name
        self.__age = age
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def surname(self):
        return self.__surname

    @age.setter
    def age_change(self, new_age):
        self.__age = new_age
        return self.__age


ex1 = Person('Bob', '99', 'Marlie')
print(ex1.name)
print(ex1.surname)
print(ex1.age)

ex1.age_change = '999'
print(ex1.age)
