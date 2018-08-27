# Easy
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:

    def __init__(self, car_model, car_speed, car_color, car_is_police):
        self.name = car_model
        self.speed = car_speed
        self.color = car_color
        self.is_police = False

    def startengine(self):
        print(self.name, 'start engine...')

    def gogo(self):
        print(self.name, 'start go!!!')

    def stopcar(self):
        print(self.name, 'is stop!!!')

    def turn(self, direction):
        print(self.name, 'is turn on {}'.format(direction))


class SportCar:
    def __init__(self, car_model, car_speed, car_color, car_is_police):
        self.name = car_model
        self.speed = car_speed
        self.color = car_color
        self.is_police = False

    def startengine(self):
        print(self.name, 'start engine...')

    def gogo(self):
        print(self.name, 'start go!!!')

    def stopcar(self):
        print(self.name, 'is stop!!!')

    def turn(self, direction):
        print(self.name, 'is turn on {}'.format(direction))


class WorkCar:
    def __init__(self, car_model, car_speed, car_color, car_is_police):
        self.name = car_model
        self.speed = car_speed
        self.color = car_color
        self.is_police = False

    def startengine(self):
        print(self.name, 'start engine...')

    def gogo(self):
        print(self.name, 'start go!!!')

    def stopcar(self):
        print(self.name, 'is stop!!!')

    def turn(self, direction):
        print(self.name, 'is turn on {}'.format(direction))


class PoliceCar:
    def __init__(self, car_model, car_speed, car_color, car_is_police):
        self.name = car_model
        self.speed = car_speed
        self.color = car_color
        self.is_police = True

    def startengine(self):
        print(self.name, 'start engine...')

    def gogo(self):
        print(self.name, 'start go!!!')

    def stopcar(self):
        print(self.name, 'is stop!!!')

    def turn(self, direction):
        print(self.name, 'is turn on {}'.format(direction))


mini = TownCar('Mini for two', '140 km/h', 'red', False)
mini.gogo()
mini.turn('left')
print(mini.name)
print('Max speed', mini.speed)
print('Car color is', mini.color)
mini.stopcar()
print('Is it police? =', mini.is_police)


# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class Car:
    def __init__(self, car_model, car_speed, car_color, car_is_police):
        self.name = car_model
        self.speed = car_speed
        self.color = car_color
        self.is_police = False

    def startengine(self):
        print(self.name, 'start engine...')

    def gogo(self):
        print(self.name, 'start go!!!')

    def stopcar(self):
        print(self.name, 'is stop!!!')

    def turn(self, direction):
        print(self.name, 'is turn on {}'.format(direction))


class TownCar(Car):
    pass


class SportCar(Car):
    pass

class WorkCar:
    pass


class PoliceCar:
    pass


mini = TownCar('Mini for two', '140 km/h', 'red', False)
mini.gogo()
mini.turn('left')
print(mini.name)
print('Max speed', mini.speed)
print('Car color is', mini.color)
mini.stopcar()
print('Is it police? =', mini.is_police)

z4 = SportCar('BMW Z4', '250 km/h', 'white', False)
z4.gogo()
z4.turn('left')
print(z4.name)
print('Max speed', z4.speed)
print('Car color is', z4.color)
z4.stopcar()
print('Is it police? =', z4.is_police)


# Normal
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.
class Person:

    def __init__(self, health, damage, armor):
        self.health = health
        self.damage = damage
        self.armor = armor

    def calculate_damage(self, damage, armor):
        self.damage = damage
        self.armor = armor
        return damage // armor

    def attack(self, other, damage=50, armor=0.7):
        self.damage = damage
        self.armor = armor
        damage = self.calculate_damage(self.damage, self.armor)
        other.health -= damage
        print(
            '{} нанес {} урона {}, у {} осталось {} жизней.'.format(self.name, other.name, other.damage, other.name,
                                                                    other.health))


class Player(Person):
    def __init__(self, name, health=100, damage=50, armor=0.7):
        super().__init__(health, damage, armor)
        self.name = name


class Enemy(Person):
    def __init__(self, name, health=100, damage=50, armor=0.7):
        super().__init__(health, damage, armor)
        self.name = name


def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            break
        enemy.attack(player)

    if player.health > 0:
        print('Игрок победил!')
    else:
        print('Враг победил!')


player = Player('Игрок')
print(player.name, player.health)
enemy = Enemy('Враг')
print(enemy.name, enemy.health)

battle(player, enemy)

# HARD
# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка
