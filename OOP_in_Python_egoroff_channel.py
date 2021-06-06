"""
Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
В классе Counter нужно определить метод start_from, который принимает один
необязательный аргумент - значение, с которого начинается подсчет,
по умолчанию равно 0
Также нужно создать метод increment, который увеличивает счетчик на 1.
Затем необходимо создать метод display, который печатает фразу
"Текущее значение счетчика = <value>" и метод reset,
который обнуляет экземпляр счетчика

Пример работы с классом Counter
c1 = Counter()
c1.start_from()
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display() # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"
"""
class Counter:

    def start_from(self, count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.count}")

    def reset(self):
        self.count = 0

"""
Создайте класс Point. У этого класса должны быть
метод set_coordinates, который принимает координаты по x и по y, 
и сохраняет их в экземпляр класса соответственно в атрибуты x и y 
метод get_distance, который обязательно принимает экземпляр класса 
Point и возвращает расстояние между двумя точками по теореме Пифагора. 
В случае, если в данный метод передается не экземпляр класса Point 
необходимо вывести сообщение "Передана не точка"
Пример работы с классом Point
p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"
"""
class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print(f'Передана не точка')

"""
Создайте класс Laptop, у которого есть:
конструктор __init__, принимающий 3 аргумента: brand, model, price . 
Также во время инициализации необходимо создать атрибут laptop_name - 
строковое значение, вида "<brand> <model>"
hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.laptop_name) # выводит "hp 15-bw0xx"
И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.
"""
class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


laptop1 = Laptop('Apple', 'Macbook Air', 974)
laptop2 = Laptop('Apple', 'Macbook Pro', 1220)

"""
Создайте класс SoccerPlayer, у которого есть:
конструктор __init__, принимающий 2 аргумента: name, surname. 
Также во время инициализации необходимо создать 2 атрибута экземпляра: goals 
и assists - общее количество голов и передач игрока, изначально 
оба значения должны быть 0
метод score, который принимает количество голов, забитых игроком, 
по умолчанию данное значение равно единице. Метод должен увеличить 
общее количество забитых голов игрока на переданное значение;
метод make_assist, который принимает количество передач, 
сделанных игроком за матч, по умолчанию данное значение равно единице. 
Метод должен увеличить общее количество сделанных передач игроком на переданное значение;
метод statistics, который вывод на экран статистику игрока в виде:
<Фамилия> <Имя> - голы: <goals>, передачи: <assists>
leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"
"""
class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')

"""
Создайте класс Zebra, внутри которого есть метод which_stripe , 
который поочередно печатает фразы "Полоска белая", "Полоска черная", 
начиная именно с фразы "Полоска белая"
Пример работы с классом Zebra

z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"
"""
class Zebra():

    def __init__(self, count=0):
        self.count = count

    def which_stripe(self):
        self.count += 1
        if self.count % 2 == 0:
            print("Полоска черная")
        else:
            print("Полоска белая")

"""
Создайте класс Person, у которого есть:
конструктор __init__, принимающий 3 аргумента: first_name, last_name, age. 
метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
метод is_adult, который возвращает True, если человек достиг 18 лет 
и False в противном случае;
p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"
"""
class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

