from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime


def show_path_info(directory):
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = strftime("%d.%m.%Y %H:%M", localtime(filetime))
            filesize = getsize(filepath)
            parent_dir = dirname(filepath)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


if __name__ == '__main__':
    show_path_info('.')