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


# class MyResume:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#
#
# class MyResumeSlots:
#     __slots__ = ('name', 'address')
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address


mr = Person("иван", "иванов")
print(mr.__dict__)
print(asizeof.asizeof(mr))
#mr.surname = 'фамилия'
#print(mr.__dict__)
#print(asizeof.asizeof(mr))

mrs = PersonSlot("иванов", "иванов")
print(mrs.__slots__)

#mrs.surname = 'фамилия'

print(asizeof.asizeof(mr))
print(asizeof.asizeof(mrs))