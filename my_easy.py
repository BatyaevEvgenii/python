def create_dir():
    import os

    name_dir = input('Введите новое имя папки: ')
    dir_new = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(dir_new)
        print('Папка {} успешно создана'.format(dir_new))
    except FileExistsError:
        print('Папка {} уже существует'.format(dir_new))


def delete_dir():
    import os

    name_dir = input('Введите имя директории для удаления: ')
    if os.path.isdir(name_dir) == True:
        try:
            os.rmdir(name_dir)
            print('Папка {} успешно удалена'.format(name_dir))
        except OSError:
            print('Папку {} невозможно удалить'.format(name_dir))
    else:
        print('Нет такой папки')

def view_file():
    import os

    for file in os.listdir(os.getcwd()):
        print(file)


def goto_dir():
    import os

    name_dir = input('Введите имя папки: ')
    if os.path.isdir(name_dir) == True:
        os.chdir(name_dir)
        print('Успешно перешел в папку {}'.format(os.getcwd()))
    else:
        print('Невозможно перейти')

