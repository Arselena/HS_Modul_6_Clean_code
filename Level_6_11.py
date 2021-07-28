# 6.11. Время жизни переменных

# 1. Задача 3. Освобождение Государства Квадратов
# было
    for i in range(len(battalion)):  
        assert type(battalion[i]) is int and battalion[i] >= 0 
    assert len(battalion) == L*2 
    # много кода без переменной battalion
    if len(battalion) % 2 == 0:
        L = len(battalion)
    else:
        L = len(battalion) - 1
    for i in range(0, L, 2):
        assert battalion[i] <= N  
        assert battalion[i+1] <= M 
        Squares[battalion[i]-1][battalion[i+1]-1] = 2
# стало. Группируем код с переменной battalion, сужая окно уязвимости
    # много кода без переменной battalion
    for i in range(len(battalion)): 
        assert type(battalion[i]) is int and battalion[i] >= 0 
    assert len(battalion) == L*2 
    if len(battalion) % 2 == 0:
        L = len(battalion)
    else:
        L = len(battalion) - 1
    for i in range(0, L, 2):
        assert battalion[i] <= N  
        assert battalion[i+1] <= M
        Squares[battalion[i]-1][battalion[i+1]-1] = 2

# 2. Задачв 20. Делаем национальный редактор "Лапоть"
# было
    S_current = ""  # Текущая строка
    list_chang = []  # Список изменений
    list_redo = []  # Список для отмены отмены
    be_chang = False  # Признак, что были изменения

    def BastShoe(command:str):
        global S_current, list_chang, list_redo, be_chang  # Помечаем глобальные переменные, что позволит записывать в них новые значения. Важно это сделать в начале ф-ии
# стало. Вместо глобальных переменных используем класс
    class editor:
        def __init__(self)
            self.S_current = ""  # Текущая строка
            self.list_chang = []  # Список изменений
            self.list_redo = []  # Список для отмены отмены
            self.be_chang = False  # Признак, что были изменения

# 3. Модуль 5. Алгоритмы. Задача 1.
# было
    class Node:  # Node будут два элемента: value (само данное) и next -- "связь", по сути указатель на следующий узел. 
        def __init__(self, v):
            self.value = v
            self.next = None

# стало. Сделаем next приватной переменной
    class Node:
        def __init__(self, v):
            self.value = v
            self.__next = None

# 4. Модуль 5. Алгоритмы. Задача 4.
# было
    class Oper:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.res = 0
# стало. Сделаем next приватной переменной
    class Oper:
        def __init__(self, a, b):
            self.a = a
            self.b = b
            self.__res = 0

# 5. Модуль 5. Задача 6. Двусторонняя очередь (deque)
# было
    class Deque:
        def __init__(self):  # инициализация внутреннего хранилища
            self.deque = []
# стало. Сделаем deque приватной
    class Deque:
        def __init__(self):  # инициализация внутреннего хранилища
            self.__deque = []

# 6. Модуль 5. Задача 10
# было
    class PowerSet:
        def __init__(self):  # ваша реализация хранилища
            self.values_list = [] # список для внутреннего хранения
# стало. Сделаем values_list приватной
    class PowerSet:
        def __init__(self): 
            self.__values_list = [] 
# 7. Модуль 5. Задача 12. Кэш
# было
    class NativeCache:
        def __init__(self, sz):
            self.size = sz
            self.slots = [None] * self.size  # массив ключей
            self.values = [None] * self.size  # массив значений
            self.hits = [0] * self.size  # массив кол-ва обращений
# стало. Сделаем hits приватной
    class NativeCache:
        def __init__(self, sz):
            self.size = sz
            self.slots = [None] * self.size  # массив ключей
            self.values = [None] * self.size  # массив значений
            self.__hits = [0] * self.size  # массив кол-ва обращений

# 8. Задача взята с https://github.com/Vladimir-82/slill_box_7/blob/91dd0c90c186e4673d5e5f6f08eee58ae0efec23/alchemy.py
# было
    class Water:
        def __init__(self):
            self.name = 'Вода'
# стало. Сделаем name приватной переменной
    class Water:
        def __init__(self):
            self.__name = 'Вода'

# 9. Задача взята с https://github.com/Python18Academy/python_first_level/blob/9ce490da3108474b135a17086f4d11f2a3bbbe55/11.%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20OOP%20%20%20%D0%9D%D0%BE%D0%B2%D0%B0%D1%8F%20%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%8F/code__11__python/9_tesla_car_9.py
# было
    class Car:
        """Базовый класс автомобиля"""
        def __init__(self, marka, speed):
            """ инициализирует атрибуты марки и скорости автомобиля"""
            self.marka = marka
            self.speed = speed
            self.odometr_reading = 0
        # много кода
        def read_odometr(self):
            """Выведет нам пробег автомобиля """
            print("У этого автомобиля пробег " + str(
                self.odometr_reading) + " на счетчике")
# стало. Сделаем odometr_reading приватной переменной
    class Car:
        """Базовый класс автомобиля"""
        def __init__(self, marka, speed):
            """ инициализирует атрибуты марки и скорости автомобиля"""
            self.marka = marka
            self.speed = speed
            self.__odometr_reading = 0
        # много кода
        def read_odometr(self):
            """Выведет нам пробег автомобиля """
            print("У этого автомобиля пробег " + str(
                self.__odometr_reading) + " на счетчике")

# 10. код взят с https://github.com/neur0tr0n/netology-PYDA-16/blob/f9287af2188bc1fea4338dfe3c3e2c88d129c5e6/HomeWork1/homework_pyda_01_06.py
# было
    import math
    print('Расчет площади фигуры.')
    figure_type = int(input('Введите тип фигуры: 1 - круг, 2 - треугольник, 3 - прямоугольник: '))
    if figure_type == 1:
        print('Вы выбрали рачет плащади круга.')
        radius = float(input('Введите значение радиуса круга: '))
        area = round(math.pi * pow(radius, 2), 2)
        print(f'Площадь круга равна: {area}')
    elif figure_type == 2:
        print('Вы выбрали рачет плащади треугольника.')
        side_a = float(input('Введите зачение длины 1 стороны: '))
        side_b = float(input('Введите зачение длины 2 стороны: '))
        side_c = float(input('Введите зачение длины 3 стороны: '))
        sp = (side_a + side_b + side_c) / 2
        area = round(math.sqrt(sp * (sp - side_a) * (sp - side_b) * (sp - side_c)), 2)
        print(f'Площадь треугольника равна: {area}')
    else:
        print('Вы выбрали рачет плащади прямоугольника.')
        side_a = float(input('Введите зачение длины 1 стороны: '))
        side_b = float(input('Введите зачение длины 2 стороны: '))
        area = round(side_a * side_b, 2)
        print(f'Площадь прямоугольника равна: {area}')
# стало. Расчеты площади сгруппированы в отдельные ф-ии
    import math
    def calculating_circle():
        print('Вы выбрали рачет плащади круга.')
        radius = float(input('Введите значение радиуса круга: '))
        area = round(math.pi * pow(radius, 2), 2)
        return area

    def calculating_triangle():
        print('Вы выбрали рачет плащади треугольника.')
        side_a = float(input('Введите зачение длины 1 стороны: '))
        side_b = float(input('Введите зачение длины 2 стороны: '))
        side_c = float(input('Введите зачение длины 3 стороны: '))
        sp = (side_a + side_b + side_c) / 2
        area = round(math.sqrt(sp * (sp - side_a) * (sp - side_b) * (sp - side_c)), 2)
        return area

    def calculating_rectangle():
        print('Вы выбрали рачет плащади прямоугольника.')
        side_a = float(input('Введите зачение длины 1 стороны: '))
        side_b = float(input('Введите зачение длины 2 стороны: '))
        area = round(side_a * side_b, 2)
        return area

    print('Расчет площади фигуры.')
    figure_type = int(input('Введите тип фигуры: 1 - круг, 2 - треугольник, 3 - прямоугольник: '))
    if figure_type == 1:
        print(f'Площадь фигуры равна: {calculating_circle()}')
    elif figure_type == 2:
        print(f'Площадь треугольника равна: {calculating_triangle()}')
    else:
        print(f'Площадь прямоугольника равна: {calculating_rectangle()}')

# 11. Код взят с https://github.com/FDmitry82/Python-interview/blob/526dd2af4278d604983d0ac110de1f16f7eb1259/01/task_4.py
# было
    print('Добро пожаловать в интернет-банк!')
    print('У нас фантастические процентные ставки!')
    print('На какую сумму желаете сделать вклад?')
    money = float(input())
    print('На какой срок желаете сделать вклад?')
    times = float(input())
    # Депозит до 10 000 руб
    if (money<9999 and times < 6):
        moneys = (money * 0.05 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    elif (money<9999 and times < 12):
        moneys = (money * 0.06 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    elif (money<9999 and times < 24):
        moneys = (money * 0.05 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    # Депозит до 100 000 руб
    elif (money<99999 and times < 6):
        moneys = (money * 0.006 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    elif (money<99999 and times < 12):
        moneys = (money * 0.007 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    elif (money<99999 and times < 24):
        moneys = (money * 0.0065 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    # Депозит до 1 000 000 руб
    elif (money<1000000 and times < 6):
        moneys = (money * 0.007 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    elif (money<1000000 and times < 12):
        moneys = (money * 0.008 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')
    elif (money<1000000 and times < 24):
        moneys = (money * 0.0075 * times) + money
        print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
        print('К концу срока Вы получаете', moneys, '₽.')

# стало. Расчеты по депозиту сгруппированы в отдельную ф-ии
    def calculation_deposit(money, times):
        if (money<9999 and times < 6):
            moneys = (money * 0.05 * times) + money
        elif (money<9999 and times < 12):
            moneys = (money * 0.06 * times) + money
        elif (money<9999 and times < 24):
            moneys = (money * 0.05 * times) + money
        # Депозит до 100 000 руб
        elif (money<99999 and times < 6):
            moneys = (money * 0.006 * times) + money
        elif (money<99999 and times < 12):
            moneys = (money * 0.007 * times) + money
        elif (money<99999 and times < 24):
            moneys = (money * 0.0065 * times) + money
        # Депозит до 1 000 000 руб
        elif (money<1000000 and times < 6):
            moneys = (money * 0.007 * times) + money
        elif (money<1000000 and times < 12):
            moneys = (money * 0.008 * times) + money
        else (money<1000000 and times < 24):
            moneys = (money * 0.0075 * times) + money
        return moneys
    print('Добро пожаловать в интернет-банк!' \n
        'У нас фантастические процентные ставки!'\n
        'На какую сумму желаете сделать вклад?')
    money = float(input())
    print('На какой срок желаете сделать вклад?')
    times = float(input())
    print(f'Депозит: {money}, Срок вклада: {int(times)} месяцев')
    print('К концу срока Вы получаете', calculation_deposit(money, times), '₽.')

# 12. Код взят с https://github.com/DuDaria/Homework_backend/blob/fa9e06e79c7b61896e53417e8b91fd69e87d6061/lesson_7/hw07_hard.py
# было
    import os
    class Job:
        def __init__(self, job_name, workers, hours_of):
            self.job_name = job_name
            self.workers = workers
            self.hours_of = hours_of 
        def sallary_worker(self):   
            for hours in self.hours_of:
                for worker in self.workers:
                    if worker.l_name == hours.l_name:
                        if int(worker.hour_rate) < int(hours.work_hours):
                            # стоимость часа
                            cost_hour = int(worker.salary) / int(worker.hour_rate)

                            # переработка часов
                            sallary_hours = (int(hours.work_hours) - \
                                            int(worker.hour_rate))* cost_hour

                            # Расчет зарплаты за месяц
                            sallary_in_month = ((int(worker.salary) * int(hours.work_hours)) / \
                                                    int(worker.hour_rate)) + sallary_hours
                            
                            print("Сотрудник переработавший норму:")
                            print(f"Фамилия и Имя: {worker.get_full_name()} \n" \
                                f"Должность: {worker.get_position()} \n" \
                                f"Зарплата (руб.): {worker.get_sallary()} \n" \
                                f"Норма_часов: {worker.get_hour_rate()}\n"\
                                f"Отработано_часов: {hours.get_work_hours()} \n"\
                                f"Зарплата_в_этом_месяце (руб.): {int(sallary_in_month)}\n"
                                )

                        elif worker.hour_rate >= hours.work_hours:
                            sallary_in_month = (int(worker.salary) * int(hours.work_hours)) / \
                                                int(worker.hour_rate)

                            print(f"Фамилия и Имя: {worker.get_full_name()} \n" \
                                f"Должность: {worker.get_position()} \n" \
                                f"Зарплата (руб.): {worker.get_sallary()} \n" \
                                f"Норма_часов: {worker.get_hour_rate()}\n"\
                                f"Отработано_часов: {hours.get_work_hours()} \n"\
                                f"Зарплата_в_этом_месяце (руб.): {int(sallary_in_month)}\n"
                                )
                    else:
                        False

# стало. расчет переработки и расчет з/пл сгруппированы в отдельные ф-ии
    class Job:
        def __init__(self, job_name, workers, hours_of):
            self.job_name = job_name 
            self.workers = workers  
            self.hours_of = hours_of 

        def sallary_worker(self): # ф-ия расчета переработки
            def calculating_recycling(hours_worked): # расчет переработки (отработано часов  - норма часов)
                # много кода
                return hours_recycling
            def calculating_sallary_recycling_YES(hours_recycling): # расчет з/пл с учетом переработки
                # много кода
                return sallary_in_month
            def calculating_sallary_recycling_NO(hours_recycling): # расчет з/пл с учетом недоработки
                # много кода
                return sallary_in_month

            for worker in self.workers:
                hours_recycling = calculating_recycling(hours_worked) # часы переработки
                if  hours_recycling = 0:
                    sallary_in_month = worker.salary # = оклад
                elif hours_recycling > 0
                    sallary_in_month = calculating_sallary_recycling_YES(hours_recycling)
                else:
                    sallary_in_month = calculating_sallary_recycling_NO(hours_recycling)

                print(f"Фамилия и Имя: {worker.get_full_name()} \n" \
                        f"Должность: {worker.get_position()} \n" \
                        f"Зарплата (руб.): {worker.get_sallary()} \n" \
                        f"Норма_часов: {worker.get_hour_rate()}\n"\
                        f"Отработано_часов: {hours.get_work_hours()} \n"\
                        f"Зарплата_в_этом_месяце (руб.): {int(sallary_in_month)}\n"
                    )
# 13. Код взят с https://github.com/DuDaria/Homework_backend/blob/fa9e06e79c7b61896e53417e8b91fd69e87d6061/lesson_8/hw08_(Game_Loto).py
# было.
    class Game:
        def start(self): 
            print("Игра началась!")
            barrels = Barrel.create_barrel()
            print("Всего {} боченков".format(len(barrels)))
            self.user = Card.create_card()
            self.comp = Card.create_card()

            while True:
                self.card_user()
                self.card_comp()

                if self.result() == 0:
                    barrel = barrels.pop()
                    print("Выпал боченок № {}.\nОсталось {} боченков.".format(barrel, len(barrels)))
                    choice = input("Для выхода нажмите 'q'.\nЗачеркнуть цифру? (y/n): ")

                    if choice == 'y':
                        correct_answer = False
                        for x in self.user:
                            for y in x:
                                if y == barrel:
                                    x[x.index(y)] = '-' 
                                    correct_answer = True
                        if not correct_answer:
                            print("Боченка № {} нет в вашей карточке!\nВы проиграли!".format(barrel))
                            print("Игра окончена!")
                            break

                    elif choice == 'n':
                        correct_answer = True
                        for x in self.user:
                            for y in x:
                                if y == barrel:
                                    correct_answer = False
                        if not correct_answer:
                            print("Бочонок № {} был в вашей карточке!\nВы проиграли!".format(barrel))
                            print("Игра окончена!")
                            break

                    elif choice == 'q':
                        print("Игра окончена!")
                        break
                    else:
                        print("Вы ввели не правильное значение!")
                        print("Игра окончена!")
                        break
                    
                elif self.result == 1:
                    break
                elif self.result == 2:
                    break
                elif self.result == 3:
                    break
                else:
                    break

                for x in self.comp:
                    for y in x:
                        if y == barrel:
                            x[x.index(y)] = '-' 
# стало. Поиск наличия цифры в карточке сгруппирован в отдельную ф-ию
    class Game:
        def start(self): 
            print("Игра началась!")
            barrels = Barrel.create_barrel()
            print("Всего {} боченков".format(len(barrels)))
            self.user = Card.create_card()
            self.comp = Card.create_card()

            def barrel_in_card(barrel): # наличие цифры к карточке
                correct_answer = False
                for x in self.user:
                    for y in x:
                        if y == barrel:
                            x[x.index(y)] = '-' 
                            correct_answer = True
                return correct_answer
        
            while True:
                self.card_user()
                self.card_comp()
                if self.result() == 0:
                    barrel = barrels.pop()
                    print("Выпал боченок № {}.\nОсталось {} боченков.".format(barrel, len(barrels)))
                    choice = input("Для выхода нажмите 'q'.\nЗачеркнуть цифру? (y/n): ")

                    if choice == 'y':
                        correct_answer = barrel_in_card(barrel)
                        if not correct_answer:
                            print("Боченка № {} нет в вашей карточке!\nВы проиграли!".format(barrel))
                            print("Игра окончена!")
                            break

                    elif choice == 'n':
                        correct_answer = barrel_in_card(barrel)
                        if not correct_answer:
                            print("Бочонок № {} был в вашей карточке!\nВы проиграли!".format(barrel))
                            print("Игра окончена!")
                            break
        # много кода
# 14. Код взят с https://github.com/grajdaninrossii/hockey_project/blob/ea99a346ad1f73a4adad24e44b5634896127cda4/Kuzin_task_2.py
# было 
    # Программа, анализирующая статистику игр КХЛ
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    import sys

    def load_cvs_file():
        global season, source_data, team_1, team_2
        season = input("Введите название сезона (например 2013_14): ") # Ввод названия сезона
        name_file ="khl_" + season + ".csv" # Конструирование пути к сsv файлу
        print(name_file)
        try: # обработка исключения, если файл не будет найден
            source_data = pd.read_csv(name_file, delimiter = ',') # Исходные данные из csv-файла(создание датафрейма)
        except Exception:
            print("Ошибка ввода названия сезона!\nЗавершение работы программы")
            sys.exit(0) # Завершение работы программы
# стало. Вместо глобальных переменных используем класс
    class KHL:
        def __init__(season, source_data, team_1, team_2):
            self.season = season
            self.source_data = source_data
            self.team_1 = team_1
            self.team_2 = team_2
    # много кода переделать для работы с классом

# 15. Код взят с https://github.com/tretyakovr/sobes_Lesson02/blob/bc743642f78f5d340283ab57b8d1ce3c9c85f5d6/Lesson02.py
# было
    class ItemDiscount:
        def __init__(self, name, price):
            self.name = name
            self.price = price
# стало. Сделаем price приватной переменной
    class ItemDiscount:
        def __init__(self, name, price):
            self.name = name
            self.__price = price
