# 6.5. Имена классов. Т.к. у меня нет подходящего кода с классами, то код для задания найден с GitHub 
# 3.1. Улучшите пять имён классов в вашем коде.
# 1. Строка 19. HistoryPerson() -> Person()
# 2. Строка 51. Add_info(HistoryPerson) -> HistoryPerson(Person)
# 3. Строка 114. My_list -> Sequence
# 4. Строка 171. CurrencyClass -> Currency
# 5. Строки 196 и 218. EURClass -> EUR_to_RUB; USDClass -> USD_to_RUB
# 3.2. Улучшите семь имён методов и объектов по схеме из пункта 2.
# 1. Строка 75. gainCountry -> getCountry
# 2. Строка 77. gainAge -> getAge
# 3. Строка 63. Age -> getAge
# 4. Стпрка 127. first -> getFirstItem
# 5. Строка 109. __new__ -> __init__
# 6. Строки 186, 208, 230. info -> getInfo  // метод д.б. глаголом
# 7. Строки 183, 205, 227. converter -> convert  // метод д.б. глаголом

# https://github.com/Vitalton/python_labs/blob/b62aa7d9e59096feac67aa278ba178dc27b161f4/lab12.py
import random
class HistoryPerson():
    '''СПЕЦИАЛЬНЫЕ МЕТОДЫ'''
    def __init__(self, surname, industry):
        self.__surname = surname # АТРИБУТ "Только для чтения"
        self.industry = industry
        self.year_birth = random.randint(1580, 1630)
        self.year_death = random.randint(1630, 1680)
        if (self.year_death - self.year_birth) > 24:
            self.year_birth -= 10
            self.year_death += 10
    def __str__(self):
        return self.__surname + " - это историческая личность, которая внесла большой вклад в развитие науки"
    def __del__(self):
        print("Экземпляр удалён!")

    '''СТАТИЧЕСКИЙ МЕТОД'''
    def status(self):
        print("Инфо о исторической личности:")
        print("Фамилия:", self.__surname)

    '''ЗАКРЫТЫЙ МЕТОД'''
    def __privateMethod(self):
        print("Эти данные недоступны пользователю!")

    '''МЕТОД ЭКЗЕМПЛЯРА КЛАССА'''
    def setYear(self, year):
        if year >= 1580 and year <= 1680:
            return year
        else:
            print("Введено некорректное значение!")

# КЛАСС-НАСЛЕДНИК
class Add_info(HistoryPerson):
    def __init__(self, surname, name, industry):
        super().__init__(surname, industry)
        self.name  = name

    def setYear(self, year):
        if year >= 1580 and year <= 1630:
            self.year_birth = year
        if year >= 1630 and year <= 1680:
            self.year_death = year
        else:
            print("Введено некорректное значение!")
    def age(self):
        return self.year_death - self.year_birth
    def getInfo(self):
        print("Фамилия: ", self._HistoryPerson__surname, "\n" + "Имя: ", self.name, "\n" + "Отрасль: ",
              self.industry, "\n" + "Год рождения: ",
              self.year_birth, "\n" + "Год смерти: ",
              self.year_death, "\n" + "Возраст: ",
              self.age(), "\n")

# ПОЛЬЗОВАТЕЛЬСКИЙ КЛАСС
class Generate():
    countries = ("Великобритания", "Германия", "Франция", "Италия", "Испания", "Нидерланды")
    def gainCountry(self):
        return random.choice(self.countries)
    def gainAge(self):
        return random.randint(1, 2020)

# КЛАСС МНОЖЕСТВЕННГО НАСЛЕДОВАНИЯ
class Human(Add_info, Generate):
    def __init__(self, surname, name, industry):
        super().__init__(surname, name, industry)
        self.country = self.gainCountry()
        self.year_birth = self.gainAge()
        self.year_death = self.gainAge()
        if self.age() < 0:
            self.year_death += 2000
            if self.year_death > 2020:
                self.year_death = 2020
        if self.age() > 100:
            print("Возраст превышает среднюю макс. продолжительность жизни!\nИзмените годы жизни "
                  "вручную!")
            print("Год рождения: ",
              self.year_birth, "\n" + "Год смерти: ",
              self.year_death, "\n" + "Возраст: ",
              self.age(), "\n")
            print("1. Изменить год рождения\n2. Изменить год смерти\n3. Человек жив!")
            option = input("Введите номер операции: ")
            if option == "1":
                self.year_birth = int(input("Введите год рождения: "))
            if option == "2":
                self.year_death = int(input("Введите год смерти: "))
            if option == "3":
                self.year_death = 2020

# НАСЛЕДОВАНИЕ ОТ НЕИЗМЕНЯЕМОГО КЛАССА
class Converter(float):
    def __new__ (cls,arg):
        arg *= 3.28
        return round(arg, 2)

# КЛАСС-ПОСЛЕДОВАТЕЛЬНОСТЬ
class My_list():
    ''' Пользовательский класс, близкий к списку '''
    def __init__ (self, values = None) :
        if values is None :
            self.values = []
        else:
            self.values = values
    def __getitem__ (self, key):
        ''' Получить значение по ключу '''
        return self.values[key]
    def __setitem__ (self, key, value):
        ''' Установить значение по ключу '''
        self.values[key] = value
    def first (self):
        ''' Получить значение первого элемента '''
        return self.values[0]
    def __iter__(self):
        ''' Сделать последовательность итерабельной '''
        return iter(self.values)
    def __str__(self):
        ''' Возвратить строковое представление объекта '''
        return "Мой список: " + str(self.values)


Newton = Add_info("Ньютон", "Исаак", "Физика")
Newton.getInfo()
Newton.setYear(1674)
Newton.getInfo()

Me = Human("Молчанов", "Виталий", "Программирование")
Me.getInfo()
print("Страна рождения: ", Me.country)
print("\n")

num = int(input("Введите длину в метрах: "))
print("Длина в футах: ", Converter(num))
print("\n")

list1 = My_list([1,5,3,7,"list"])
print(list1)
print("Ваш элемент: ", list1[4])
list1[4] = 252
print("Ваш элемент: ", list1[4])
print("Первый элемент: ", list1.first())
print("Итерабельная последовательность: ")
for i in list1:
    print (i, end= ' ')
print("\n")

# https://github.com/GeorgiyDemo/FA/blob/f10539200b36515ed4d73cbb02f8b46b26f98d68/Course%20I/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D1%8B%20Python/Part2/%D1%81%D0%B5%D0%BC%D0%B8%D0%BD%D0%B0%D1%80%D1%8B/pract1/second/task14.py
"""
Задача 14. Создайте класс ВАЛЮТА с методами перевода денежной суммы в рубли и вывода на экран.
Создайте дочерние классы ДОЛЛАР, ЕВРО со своими методами перевода и вывода на экран.
Создайте список п валютных денежных сумм и выведите полную информацию о них на экран.
"""

from random import randint
class CurrencyClass:
    """
    Родительский класс с абстрактной валютой
    """
    # Стат поля
    eur_currency = 70.94
    usd_currency = 65.27

    def __init__(self, balance, exchange):
        self.balance = balance
        self.exchange = exchange

    def converter(self):
        return self.balance * self.exchange

    def info(self):
        return (
            "[Родительский класс валюты]\nКол-во: "
            + str(self.balance)
            + "\nКурс обмена: "
            + str(self.exchange)
            + "\nСконвертированная валюта: "
            + str(self.converter())
        )

class EURClass(CurrencyClass):
    """
    Класс для работы с EUR
    """

    def __init__(self, balance):
        self.currency = super().eur_currency
        self.balance = balance

    def converter(self):
        return self.balance * self.currency

    def info(self):
        return (
            "[EUR]\nКол-во EUR: "
            + str(self.balance)
            + "\nКурс обмена: "
            + str(self.currency)
            + "\nСконвертированная валюта в RUB: "
            + str(self.converter())
        )

class USDClass(CurrencyClass):
    """
    Класс для работы с USD
    """

    def __init__(self, balance):
        self.currency = super().usd_currency
        self.balance = balance

    def converter(self):
        return self.balance * self.currency

    def info(self):
        return (
            "[USD]\nКол-во USD: "
            + str(self.balance)
            + "\nКурс обмена: "
            + str(self.currency)
            + "\nСконвертированная валюта в RUB: "
            + str(self.converter())
        )

def main():
    try:
        n = int(input("Введите кол-во валютных денежных сумм -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: EURClass,
        2: USDClass,
    }

    currency_list = [d[randint(1, 2)](randint(1, 1000)) for _ in range(n)]
    for c in currency_list:
        print(c.info() + "\n")


if __name__ == "__main__":
    main()