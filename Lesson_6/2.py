"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""


from pympler import asizeof


class Person:
    """Класс для сущности человек"""
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display_information(self):
        print(self.__class__.__name__)
        print('name:', self.firstname, self.lastname)


class PersonSlot:
    """Класс для сущности человек"""
    __slots__ = ("firstname", "lastname")

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def display_information(self):
        print(self.__class__.__name__)
        print('name:', self.firstname, self.lastname)


mr = Person("иван", "иванов")
print(mr.__dict__)

mrs = PersonSlot("иванов", "иванов")
print(mrs.__slots__)

print(asizeof.asizeof(mr))
print(asizeof.asizeof(mrs))

"""
На объекта обычного класса выделено 472 байта памяти
На объекта класса с применением слотов выделено 144 байта памяти. Экономия более чем в 3 раза.
"""
