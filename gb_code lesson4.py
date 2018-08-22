# Все задачи текущего блока решите с помощью генераторов списков!

# Easy
# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# list = [24, 100, 9, 20]
# result = [i ** 2 for i in list]
# print(result)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
# list_fruits1 = ['apple', 'banana', 'kiwi', 'pear', 'grapes', 'melon', 'waterlemon', ]
# list_fruits2 = ['plum', 'cherry', 'pineapple', 'apple', 'melon', 'pear', ]
# list_fruits3 = [fru for fru in list_fruits1 if fru in list_fruits2]
# print(list_fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
# list_number = [30, 90, 33, 333, 27, 15, -12, 24, 10]
# list_num = [num for num in list_number if num > 0 and (int(num) % 3 == 0) and (int(num) % 4 != 0)]
# print(list_num)

# Normal
# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
# import re
#
# name = input('Введите имя: ')
# surname = input('Введите фамилию: ')
# pattern_name = '^([А-Я][а-я]+)'
# pattern_surname = '^([А-Я][а-я]+)'
# email = input('Введите адрес электронной почты: ')
# pattern_email = '(([a-z_\.0-9]+)@([a-zA-Z]+)\.(ru|org|com))'
#
# for name_ in name:
#     result_name = re.match(pattern_name, name)
#     if not result_name:
#         print('Неверное указано имя!')
#         name = input('Введите имя: ')
#     else:
#         pass
#
# for surname_ in surname:
#     result_surname = re.match(pattern_surname, surname)
#     if not result_surname:
#         print('Неверное указана фамилия!')
#         surname = input('Введите фамилию: ')
#     else:
#         pass
#
# for mail in email:
#     result_email = re.match(pattern_email, email)
#     if not result_email:
#         print('Неверное указан e-mail!')
#         email = input('Введите адрес электронной почты: ')
#     else:
#         pass
#
# print(result_name.group(1))
# print(result_surname.group(1))
# print(result_email.group(1))


# Задача - 2:
# Вам дан текст:
# import re
#
# some_str = '''
# Мороз и солнце; день чудесный!
# Еще ты дремлешь, друг прелестный —
# Пора, красавица, проснись:
# Открой сомкнуты негой взоры
# Навстречу северной Авроры,
# Звездою севера явись!
# Вечор, ты помнишь, вьюга злилась,
# На мутном небе мгла носилась;
# Луна, как бледное пятно,
# Сквозь тучи мрачные желтела,
# И ты печальная сидела —
# А нынче. погляди в окно:
# Под голубыми небесами
# Великолепными коврами,
# Блестя на солнце, снег лежит;
# Прозрачный лес один чернеет,
# И ель сквозь иней зеленеет,
# И речка подо льдом блестит.
# Вся комната янтарным блеском
# Озарена... Веселым треском
# Трещит затопленная печь.
# Приятно думать у лежанки.
# Но знаешь: не велеть ли в санки
# Кобылку бурую запречь?
# Скользя по утреннему снегу,
# Друг милый, предадимся бегу
# Нетерпеливого коня
# И навестим поля пустые,
# Леса, недавно столь густые,
# И берег, милый для меня.
# '''
#
# # Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# # более одной точки, при любом исходе сообщите результат пользователю!
#
# pattern = '(\.\.+)'  # one point and more
# match = re.findall(pattern, some_str)
# if match:
#     print('Совпадения найдены')
# else:
#     print('Совпадений НЕТ!!!')
#
# print(match)

# HARD
# Задание:
# Эта программа являет собой упрощенный симулятор банкомата, пользователь вводит номер карты и пин код,
# в случае успеха программа предлагает меню для выбора действий, где он может проверить счет, или снять деньги.
#
# Эта задача не так похожа на другие, но она, как никогда прежде приближена к реалиям разработки общего проекта.
#
# Ваша задача исправить ошибки логики, и выполнить проверки данных, которые вводит пользователь.
# Обязательно убедитесь, что вы выполнили все проверки, попробуйте сами сломать свою программу вводя неверные данные!

# person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
# person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
# person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}
#
# bank = [person1, person2, person3]
#
#
# def get_person_by_card(card_number):
#     for person in bank:
#         if person['card'] == card_number:
#             return person
#
#
# def is_pin_valid(person, pin_code):
#     if person['pin'] == pin_code:
#         return True
#     return False
#
#
# def check_account(person):
#     return round(person['money'], 2)
#
#
# def withdraw_money(person, money):
#     if person['money'] - money > 0:
#         person['money'] -= money
#         return 'Вы сняли {} рублей.'.format(money)
#     else:
#         return 'На вашем счету недостаточно средств!'
#
#
# def process_user_choice(choice, person):
#     if choice == 1:
#         print(check_account(person))
#     elif choice == 2:
#         count = int(input('Сумма к снятию:'))
#         print(withdraw_money(person, count))
#
#
# def start():
#     card_number, pin_code = input('Введите номер карты и пин код через пробел:').split()
#
#     card_number = int(card_number)
#     pin_code = int(pin_code)
#     person = get_person_by_card(card_number)
#     if person and is_pin_valid(person, pin_code):
#         while True:
#             choice = int(input('Выберите пункт:\n'
#                                '1. Проверить баланс\n'
#                                '2. Снять деньги\n'
#                                '3. Выход\n'
#                                '---------------------\n'
#                                'Ваш выбор: '))
#             if choice == 1 or choice == 2:
#                 process_user_choice(choice, person)
#             elif choice == 3:
#                 break
#
#     else:
#         print('Номер карты или пин код введены не верно!')
#
#
# start()
