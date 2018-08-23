# Easy
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# import os

# # create directories
# count = 10
# dir_new = os.path.join(os.getcwd(), 'Dir_')
# for dir in range(count):
#     os.mkdir(dir_new + str(dir))

# # delete directories
# for dir in os.listdir(os.getcwd()):
#     if os.path.isdir(dir) == True and dir >= 'Dir_':
#         os.rmdir(dir)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# import os
# directories = [dir for dir in os.listdir(os.getcwd()) if os.path.isdir(dir)]
# print(directories)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# import os
#
# filename1 = os.path.basename(__file__)
# filename2 = filename1 + '.copy'
# # try:
# if os.path.isfile(filename2) == True:
#     os.remove(filename2)
#     print('Копия удалена')
#
# if os.name == 'posix' or os.name == 'mac':
#     os.system('cp %s %s' % (filename1, filename2))
#     print('Копия создана')
# elif os.name == 'nt':
#     os.system('copy %s %s' % (filename1, filename2))
#     print('Копия создана')
# else:
#     print('Извините, я не знаю команды для вашей системы...')


# Normal
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из my_easy.py
# import sys
# import my_easy
#
# if '1' in sys.argv:
#     print('Перейти в папку:')
#     my_easy.goto_dir()
# elif '2' in sys.argv:
#     print('Просмотреть содержимое текущей папки')
#     my_easy.view_file()
# elif '3' in sys.argv:
#     print('Внимание: удаляем папку!!!')
#     my_easy.delete_dir()
# elif '4' in sys.argv:
#     print('Создаем папку')
#     my_easy.create_dir()


# HARD
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
# import os
# import sys
#
# print('sys.argv = ', sys.argv)
#
#
# def print_help():
#     print("help - получение справки")
#     print("mkdir <dir_name> - создание директории")
#     print('cp < file_name > - создает копию указанного файла')
#     print('rm <file_name> - удаляет указанный файл (запросить подтверждение операции')
#     print('cd <full_path or relative_path> - меняет текущую директорию на указанную')
#     print('ls - отображение полного пути текущей директории')
#     print("ping - тестовый ключ")
#
#
# def make_dir():
#     if not dir_name:
#         print("Необходимо указать имя директории вторым параметром")
#         return
#     dir_path = os.path.join(os.getcwd(), dir_name)
#     try:
#         os.mkdir(dir_path)
#         print('директория {} создана'.format(dir_name))
#     except FileExistsError:
#         print('директория {} уже существует'.format(dir_name))
#
#
# def copy_file():
#     if not filename1:
#         print('Необходимо указать файл вторым параметром')
#         return
#     filename2 = filename1 + '.copy'
#     if os.path.isfile(filename2) == True:
#         os.remove(filename2)
#         print('Копия удалена')
#
#     if os.name == 'posix' or os.name == 'mac':
#         os.system('cp %s %s' % (filename1, filename2))
#         print('Копия создана')
#     elif os.name == 'nt':
#         os.system('copy %s %s' % (filename1, filename2))
#         print('Копия создана')
#     else:
#         print('Извините, я не знаю команды для вашей системы...')
#
#
# def remove_file():
#     if not filename:
#         print('Необходимо указать файл вторым параметром')
#         return
#     if os.path.isfile(filename) == True:
#         answer = input('Удалить файл? y/n: ')
#         if answer == 'y':
#             os.remove(filename)
#             print('Файл {} удален'.format(filename))
#         else:
#             return
#
#
# def change_dir():
#     if not dir_name:
#         print("Необходимо указать имя директории вторым параметром")
#         return
#     if os.path.isdir(name_dir) == True:
#         os.chdir(name_dir)
#         print('Успешно перешел в папку {}'.format(os.getcwd()))
#     else:
#         print('Невозможно перейти')
#
#
# def list_path():
#
#
#     print('Полный путь нашей папки')
#     print(os.path.abspath(os.getcwd()))
#
#
# def ping():
#     print("pong")
#
#
# do = {
#     "help": print_help,
#     "mkdir": make_dir,
#     'cp': copy_file,
#     'rm': remove_file,
#     'cd': change_dir,
#     'ls': list_path,
#     "ping": ping
# }
#
# try:
#     dir_name = sys.argv[2]
# except IndexError:
#     dir_name = None
#
# try:
#     filename1 = sys.argv[2]
# except IndexError:
#     filename1 = None
#
# try:
#     filename = sys.argv[2]
# except IndexError:
#     filename = None
#
# try:
#     name_dir = sys.argv[2]
# except IndexError:
#     name_dir = None
#
# try:
#     key = sys.argv[1]
# except IndexError:
#     key = None
#
# if key:
#     if do.get(key):
#         do[key]()
#     else:
#         print("Задан неверный ключ")
#         print("Укажите ключ help для получения справки")