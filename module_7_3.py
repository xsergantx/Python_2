"""
Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.

Задача "Найдёт везде":
Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов и
записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:
get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами,
это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла,
значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count
"""
class WordsFinder:
    # таблица преобразования для str.translate
    trans_table = str.maketrans('.!,:;=?', '       ')

    def __init__(self, *file_names: str):
        self.file_names = file_names

    def get_all_words(self):
        '''
        подготовительный метод, считывает содержимое файлов self.file_names
        и возвращает словарь с ключом названия файла и значением списка всех
        слов в файле
        '''
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding="utf-8") as file:
                content = file.read()
                content = content.lower() \
                                 .replace(' - ', ' ') \
                                 .translate(self.trans_table)
                content = ' '.join(content.split())
                all_words[file_name] = content.split()
        return all_words

    def find(self, search_word: str):
        '''
        возвращает словарь с ключом названия файла и значением первой позиции
        искомого слова
        '''
        search_word = search_word.lower()
        found_words = {}
        for file_name, words in self.get_all_words().items():
            found = False
            for i in range(len(words)):
                if words[i] == search_word:
                    found = True
                    break
            if found:
                found_words[file_name] = i + 1  # позиция начинается с 1
        return found_words

    def count(self, search_word: str):
        '''
        возвращает словарь с ключом названия файла и значением количества
        нахождений искомого слова
        '''
        search_word = search_word.lower()
        word_number = {}
        for file_name, words in self.get_all_words().items():
            word_number[file_name] = words.count(search_word)
        return word_number


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

