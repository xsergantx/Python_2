"""
Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
"Составное" в противном случае.
"""


def is_prime(func):
    def wrappper(*arf):
        res = func(*arf)
        prime = True
        for i in range (2, res - 1):
            if res % i == 0:
                prime = False
                break
        if prime:
            print('Простое')
        else:
            print('Составное')
        return res
    return wrappper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
