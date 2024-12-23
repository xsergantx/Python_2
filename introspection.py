"""
Цель задания:

Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.

Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


"""

# Домашнее задание по теме "Интроспекция"
import inspect


def introspection_info(obj):
    # Получаем тип объекта
    obj_type = type(obj).__name__

    # Получаем атрибуты объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получаем модуль, к которому принадлежит объект
    try:
        module = inspect.getmodule(obj).__name__
    except AttributeError:
        module = None

    # Возвращаем словарь с информацией
    return {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }


# Пример использования
number_info = introspection_info(42)
print(number_info)


# Создаем свой класс и объект для демонстрации
class MyClass:
    def __init__(self):
        self.attribute1 = 10
        self.attribute2 = "Hello"

    def method1(self):
        pass

    def method2(self):
        pass


my_object = MyClass()
my_object_info = introspection_info(my_object)
print(my_object_info)

info = introspection_info()
print()
pprint(info)
