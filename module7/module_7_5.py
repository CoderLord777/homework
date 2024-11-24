import os
import time

directory = os.path.abspath(os.curdir)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.abspath('module_7_5.py')
        filesize = os.path.getsize(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(filepath)
print(f'Обнаружен файл: {file},\n Путь: {filepath},\n Размер: {filesize} байт,\n Время изменения: {formatted_time},\n Родительская директория: {parent_dir}')