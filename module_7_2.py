"""
Задача "Записать и запомнить":
Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name -
название файла для записи, strings - список строк для записи.
Функция должна:
Записывать в файл file_name все строки из списка strings, каждая на новой строке.
Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
Пример полученного словаря:
{(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
Где:
1, 2 - номера записанных строк.
0, 16 - номера байт, на которых началась запись строк.
'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.

Пример результата выполнения программы:
Пример выполняемого кода:
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

Вывод на консоль:
((1, 0), 'Text for tell.')
((2, 16), 'Используйте кодировку utf-8.')
((3, 66), 'Because there are 2 languages!')
((4, 98), 'Спасибо!')
"""
def custom_write(file_name: str, strings: list):
    '''
    Функция записывает строки из strings в file_name.
    Возвращает словарь с ключом в виде кортежа с номером строки и байтом начала
    строки и значением в виде строки из strings.
    file_name - название файла для записи
    strings - список строк для записи
    '''
    strings_positions = {}
    line_number = 1
    file = open('file_name.txt', 'w', encoding="utf-8")
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        strings_positions[(line_number, line_byte)] = string
        line_number += 1
    file.close()
    return strings_positions

if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]
    result = custom_write('file_name.txt', info)
    for elem in result.items():
        print(elem)