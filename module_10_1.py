"""
Цель: понять как работают потоки на практике, решив задачу

Задача "Потоковая запись в файлы":
Необходимо создать функцию write_words(word_count, file_name), где word_count - количество записываемых слов,
file_name - название файла, куда будут записываться слова.
Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с
 прерыванием после записи каждого на 0.1 секунду.
Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

После создания файла вызовите 4 раза функцию write_words, передав в неё следующие значения:
10, example1.txt
30, example2.txt
200, example3.txt
100, example4.txt
После вызовов функций создайте 4 потока для вызова этой функции со следующими аргументами для функции:
10, example5.txt
30, example6.txt
200, example7.txt
100, example8.txt
"""


from time import sleep
from datetime import datetime
from threading import Thread

    # Объявление функции write_words
def write_words(word_count, file_name):  # где word_count - количество записываемых слов,
        # file_name - название файла, куда будут записываться слова.
    file = open(file_name, 'a', encoding='utf-8')#открытия файла в режиме записи с указанием кодировки UTF-8:
    for i in range(word_count):#счётный цикл , который повторяется определённое количество раз
        file.write(f'Какое-то слово №  {i + 1}\n')#запись в строку
        sleep(0.1)# пауза между записями
    file.close()
    print(f'Завершилась запись в файл {file_name}')#вывод строки в конце записи

# Взятие текущего времени
time_start = datetime.now()

# Запуск функций с аргументами из задачи
# После создания файла вызывается 4 раза функция wite_words
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop = datetime.now()
time_res = time_stop - time_start

# Вывод разницы начала и конца работы функций
print(f'Работа потоков {time_res}')

# После вызовов функций создайте 4 потока для вызова этой функции

# Взятие текущего времени
time2_start = datetime.now()

# Создание и запуск потоков с аргументами из задачи
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourh = Thread(target=write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourh.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourh.join()

# Взятие текущего времени

time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Работа потоков {time2_res}')




