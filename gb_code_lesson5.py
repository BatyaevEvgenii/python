# import my_game_lib
# # from my_game_lib import pow
#
# print(__name__)
# print(my_game_lib.pow(2, 2))
# print(pow(2,2))

# import lib.test

# import sys
#
# for path in sys.path:
#     print(path)

# ПОЧИТАТЬ!!!!
# import os
#
# # НЕ НАДО РАБОТАТЬ НАПРЯМУЮ С КОНСОЛЬЮ ОС!
# print(os.getcwd())
#
# # os.mkdir('test_folder')
# for file in os.listdir():
#     print(file)

import sys

print(sys.argv)

if 'help' in sys.argv:
    print('Помощь по программе:')
elif 'backup' in sys.argv:
    print('Резервное копирование')

# ДЗ от GeekBrains



