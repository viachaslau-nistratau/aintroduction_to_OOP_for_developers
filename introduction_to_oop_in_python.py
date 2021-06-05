"""
Представьте себе на секунду, что вы Бог и только что сотворили Человека.
Люди - это вид, называемый Homo Sapiens, и они (обычно) имеют 2 ноги и 2 руки.
Создайте атрибуты species, n_legs и n_arms для вашего класса Human.
Если вы правильно создали класс, приведенный ниже код выведет соответствующую информацию.
Не удаляйте код, он здесь, чтобы проверить вашу (Божью) работу!
"""
class Human:
    species = 'Homo Sapiens'
    n_legs = '2'
    n_arms = '2'


# control code, don't delete!
print(Human)
print(Human.species)
print(Human.n_arms)
print(Human.n_legs)

"""
Создайте класс Book, в котором будут атрибуты name и author, 
со значениями из input. Затем выведите значения. 
Sample Input:
Преступление и наказание
Федор Михайлович Достоевский
Страх и Трепет
Сёрен Кьеркегор
Голова профессора Доуэля
Александр Романович Беляев
Sample Output:
Преступление и наказание - Федор Михайлович Достоевский
Страх и Трепет - Сёрен Кьеркегор
Голова профессора Доуэля - Александр Романович Беляев
"""
class Book:
    all_infa = []

    def __init__(self, name, author):
        self.name = name
        self.author = author
        Book.all_infa.append(self)


for i in range(3):
    name = input()
    author = input()
    infa = Book(name, author)

    print(f'{name} - {author}')

"""
Создайте класс Movie и определите конструктор класса с такими параметрами, 
как заголовок, режиссер и год выпуска.
Затем создайте такие объекты, как «Титаник» (реж. Джеймс Кэмерон, 1997), 
«Звездные войны» (реж. Джордж Лукас, 1977) и «Бойцовский клуб» (реж. Дэвид Финчер, 1999).
Некоторые атрибуты этих объектов будут напечатаны, чтобы проверить их.
Год передается в виде строки.
"""
class Movie:
    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director


# objects of the class Movie
titanic = Movie("Титаник", "1997", "Джеймс Кэмерон")
star_wars = Movie("Звездные войны", "1977", "Джордж Лукас")
fight_club = Movie("Бойцовский клуб", "1999", "Дэвид Финчер")

# don't delete this code
# it is here to check your results
print(titanic.title)
print(star_wars.year)
print(fight_club.director)

"""
Джон работает в университете. Ему постоянно приходится иметь дело с большим 
объемом информации об учебном процессе и учениках, и поэтому он решил создать 
программу, которая поможет ему в этом.
Он разработал систему для создания идентификатора для каждого студента: 
первая буква имени, фамилия, а затем год рождения. Например, идентификатор для 
Джейдена Смита (р. 1998) будет выглядеть как JSmith1998.
Джону нужна помощь, чтобы завершить код для удостоверения личности и затем 
применить его к студентам. Создайте идентификатор атрибута экземпляра в 
методе __init__, рассчитайте его, а затем напечатайте его значение для учащегося.
Формат ввода:
Информация об ученике: первая строка имеет имя, вторая - фамилию, 
а третья - год рождения.
Формат вывода:
Идентификатор студента.
Hint: считать несколько строк из стандартного ввода можно вызвав input() несколько раз.
"""
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = "{0}{1}{2}".format(str(list(self.name)[0]), self.last_name, self.birth_year)
        print(self.id)

name = input()
last_name = input()
birth_year = input()
id = Student(name, last_name, birth_year)

"""
Создайте метод greet для класса Person, который печатает 
сообщение "Hello, I am {name}!"
Формат ввода:
Имя человека.
Формат вывода:
Вывод метода приветствуем.
"""
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am {}!".format(self.name))


person = Person(input())
Person.greet(person)

"""
Переопределите метод sail нашего класса Ship, чтобы он взял пункт 
назначения и затем сказал бы, куда движется корабль. 
Вызовите этот метод для объекта black_pearl, который определен в коде ниже.
Формат ввода:
Название страны или города, куда идет корабль.
Формат вывода:
Результат обновленного метода sail : сообщение, структурированное 
как "The {name of the ship} has sailed for {country/city}!"
"""
class Ship:
    def __init__(self, city):
        self.city = city

        # the old sail method that you need to rewrite

    def sail(self):
        print("The Black Pearl has sailed for {}!".format(self.city))


city = Ship(input())
Ship.sail(city)

"""
метод должен увеличивать количество друзей у пользователя на значение n.
"""
class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    # fix this method
    def add_friends(self, n):
        self.friends += n
        print("{} now has {} friends.".format(self.username, self.friends))

"""
Дан класс House. Создайте метод с именем paint, который бы принимал 
цвет в качестве аргумента и раскрашивал дом в этот цвет 
(то есть создает атрибут color со значением аргумента метода).
Метод не должен возвращать какие-либо значения или печатать сообщения.
"""
class House:
    def __init__(self, floors):
        self.floors = floors

    def paint (self, color):
        self.color = color

"""
Реализуйте класс PiggyBank, который представляет собой олдскульную копилку 
в форме свиньи. Он имеет два атрибута, доллары (dollars) и центы (cents), 
и их начальные значения передаются в конструктор.
Создайте метод add_money с двумя параметрами deposit_dollars и deposit_cents, 
который увеличивает сумму денег в копилке. Например, если вы положили в 
копилку меньше доллара, значение deposit_dollars равно 0. 
Метод не должен ничего печатать!
Параметры deposit_dollars и deposit_cents метода add_money могут иметь 
любое значение, но значение центов в копилке после добавления не может 
превышать 99! Если значение deposit_cents после добавления больше 99, 
вам необходимо обновить как значение в долларах, так и значение в центах!
"""
class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        if deposit_dollars >= 1:
            self.dollars += deposit_dollars

        self.cents += deposit_cents
        self.dollars += self.cents // 100
        self.cents = self.cents % 100