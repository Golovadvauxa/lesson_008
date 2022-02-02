# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,
#   проебываться

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.cat_food = 50
        self.money = 100
        self.mess = 0
        self.cat_plate = 0

    def __str__(self):
        return 'еда- {} еда у котика- {} в миске-{} деньги- {} беспорядок- {}'.format(self.food, self.cat_food,
                                                                                      self.cat_plate, self.money,
                                                                                      self.mess)


class Human:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fulness = 30
        self.happiness = 100

    def __str__(self):
        if self.fulness > 100:
            self.fulness = 100
        if self.happiness > 100:
            self.happiness = 100
        return '{}, сытость- {} счастье- {}'.format(self.name, self.fulness, self.happiness)


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        i = randint(1, 3)
        if self.house.mess >= 100:
            self.happiness -= 10
        if self.happiness <= 0:
            cprint('{} умер от горя'.format(self.name), color='red')
        if self.fulness <= 0:
            cprint('{} умер от голода'.format(self.name), color='red')
        elif self.fulness <= 10:
            self.eat()
        elif self.house.money <= 150:
            self.work()
        elif self.house.cat_food <= 10:
            self.cat_shopping()
        elif self.house.cat_plate <= 10:
            self.feed_cat()
        elif i == 1:
            self.work()
        else:
            self.gaming()

    def eat(self):
        if self.house.food >= 30:
            self.house.food -= 30
            self.fulness += 30
            cprint('{} поел'.format(self.name), color='yellow')

    def work(self):
        self.house.money += 150
        self.fulness -= 10
        cprint('{} сходил на работу'.format(self.name), color='blue')

    def gaming(self):
        self.happiness += 20
        self.fulness -= 10
        cprint('{} играл в танчики'.format(self.name), color='green')

    def feed_cat(self):
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.house.cat_plate += 10
            cprint('{} покормил кота '.format(self.name), color='blue')

    def cat_shopping(self):
        if self.house.money >= 10:
            self.house.money -= 10
            self.house.cat_food += 10
            self.fulness -= 10
            cprint('{} сходил за едой для котика'.format(self.name), color='blue')


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        i = randint(1, 6)
        if self.house.mess >= 100:
            self.happiness -= 10
        if self.happiness <= 0:
            cprint('{} умерла от горя'.format(self.name), color='red')
        if self.fulness <= 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
        elif self.fulness <= 10:
            self.eat()
        elif self.house.food <= 50:
            self.shopping()

        # elif self.house.cat_plate <= 10:
        #     self.feed_cat()
        elif self.house.mess >= 120:
            self.clean_house()
        elif i == 1:
            self.buy_fur_coat()
        elif i == 2:
            self.clean_house()
        elif i == 3:
            self.shopping()
        else:
            self.walking()

    def eat(self):
        if self.house.food >= 20:
            self.house.food -= 20
            self.fulness += 20
            cprint('{} поела'.format(self.name), color='yellow')

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.food += 50
            self.fulness -= 10
            cprint('{} сходила за продуктами'.format(self.name), color='blue')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 60
            self.fulness -= 10
            cprint('{} купила шубу'.format(self.name), color='green')

    def clean_house(self):
        if self.house.mess <= 100:
            self.house.mess = 0
            self.fulness -= 10
            cprint('{} убрала дома'.format(self.name), color='magenta')
        else:
            self.house.mess -= 100
            self.fulness -= 10
            cprint('{} убрала дома'.format(self.name), color='magenta')

    def feed_cat(self):
        if self.house.cat_food >= 10:
            self.house.cat_food -= 10
            self.house.cat_plate += 10
            cprint('{} покормила кота '.format(self.name), color='blue')

    def walking(self):
        self.happiness += 20
        self.fulness -= 10
        cprint('{} пошла проебаться'.format(self.name), color='green')

# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.mess += 5
#     serge.act()
#     masha.act()
#     cprint(serge, color='white')
#     cprint(masha, color='white')
#     cprint(home, color='grey')

# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     home.mess += 5
#     serge.act()
#     masha.act()
#     cprint(serge, color='white')
#     cprint(masha, color='white')
#     cprint(home, color='grey')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 50
        self.house = house

    def __str__(self):
        return 'Котик - {}, сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_plate >= 10:
            cprint('Котик {} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.cat_plate -= 10
        elif self.house.food >= 10:
            cprint('Котик {} спиздил колбасу!'.format(self.name), color='cyan')
            self.fullness += 20
            self.house.food -= 10
        else:
            cprint('Котик {} нет еды'.format(self.name), color='red')

    def sleep(self):
        cprint('Котик {} спал весь день '.format(self.name), color='yellow')
        self.fullness -= 10

    def tear_wallpaper(self):
        cprint('Котик {} подрал обои'.format(self.name), color='blue')
        self.house.mess += 10

    def act(self):
        if self.fullness <= 0:
            cprint('Котик {} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif 2 <= dice <= 3:
            self.tear_wallpaper()
        else:
            self.sleep()


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 4)
        if self.fulness <= 0:
            cprint('{} умер от голода'.format(self.name))
        elif (self.fulness <= 10) or (1 <= dice <= 2):
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            self.house.food -= 10
            self.fulness += 10
            cprint('{} поел'.format(self.name), color='yellow')

    def sleep(self):
        self.fulness -= 5
        cprint('{} поспал'.format(self.name), color='blue')


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)
kolya = Child(name='Коля', house=home)
murzik = Cat(name='Мурзик', house=home)

for day in range(365):
    home.mess += 5
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='white')
    cprint(masha, color='white')
    cprint(kolya, color='cyan')
    cprint(murzik, color='white')
    cprint(home, color='grey')
# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
