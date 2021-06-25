# 6.6. Имена функций/методов. Т.к. у меня нет подходящего кода с классами, то код для задания найден с GitHub 
# Выполните 12 улучшений имён функций/методов в вашем коде в формате "было - стало - ваш комментарий", и выложите на гитхаб.
# 1. Строка 46. guest -> count_of_available_seats  // подсчет свободных мест 
# 2. Строка 54. work_time -> get_work_time  // получить рабочее время ресторана
# 3. Строка 66. hookah -> get_hookah_info  // получить информацию о кальяне. В задании к задаче написано "добавьте метод заказать кальян", я бы сделала метод order_hookah(self, tobacco)
# 4. Строка 91. description_name -> get_info // получить информацию о машине (класс назван Car, поэтому слово car в методе не указываем)
# 5. Строка 96. read_odometr -> get_mileage  // получить пробег авто
# 6. Строка 100. update_odometr -> set_mileage  // установить пробег авто
# 7. Строка 120. description_battery -> get_info // получить информацию о батарее
# 8. Строка 163. delWS -> del_spaces_in_string  // удалить пробелы в строке
# 9. Строка 169. StCol -> count_St_and_Col  // подсчет строк и столбцов
# 10. Стпрка 183. arr -> create_array_for_Encoder  // создание массива для кодера
# 11. Строка 193. arr2 -> create_array_for_Coder  // создание массива для декодера
# 12. Cnhjrf 214. Shifr -> transport_array // Транспортировать массив

# https://github.com/onemanzerg/pyLearn/blob/ab6fc29bc1b492fe4efe7fe447d1c9ea8acba4f3/classes/homework_23_class_exemplars.py
"""Создайте основной класс ресторан
создайте атрибуты еды, напитков (до 5 штук)
Добавьте методы посадочных  мест, время работы, количество сотрудников
Создайте дочерний класс уголок кальяна
добавьте атрибуты сорты табака
добавьте метод заказать кальян

Если вы выполняли домашнее задание с прошлого занятия о пользователях сайта, тогда:
создайте класс администратор, который наследуется от базового пользователя
добавьте атрибут привилегии
Добавьте метод вывода перечня привилегий администратора

Доработка сегодняшнего занятия
Добавьте в класс Батарей метод разряда батареи, который принимает параметр пробега и внутри умножает
пробега на расход батареии и потом отнимает данные с атрибута батареи
Добавьте метод заряда батарей к 100% значению"""

class Restaurant():
    """Main class restaurant"""
    def __init__(self, name, food, drink, alco, lunch, water):
        """Initialize atts of restaurant"""
        self.name = name
        self.food = food
        self.drink = drink
        self.alco = alco
        self.lunch = lunch
        self.water = water
        self.free = 50

    def guest(self, free):
        """Vivodit kolichestvo svobodnih mest"""
        if free <= self.free:
            self.free -= free
            print("Осталось %s" % (self.free) + " мест")
        else:
            print("Нет мест")

    def work_time(self):
        """Output work time"""
        print("Ресторан %s" % (self.name) + " работает с 10-00 до 22-00")

class SmokeLounge(Restaurant):
    """Aspects for a lounge zone"""
    def __init__(self, musthave, alfaker, easy):
        self.musthave = musthave
        self.alfaker = alfaker
        self.easy = easy
        """Initialize parents atts"""

    def hookah(self, hook):
        if hook == self.musthave:
            print("Вы заказали кальян с табаком Мастхэв")


kfc = Restaurant('kfc', 'cheeseburger', 'cola', 'beer', 'bites', 'aqua')
kfc.work_time()
kfc.guest(0)

hookahhouse = SmokeLounge()
hookahhouse.hookah('alfaker')


# https://github.com/onemanzerg/pyLearn/blob/ab6fc29bc1b492fe4efe7fe447d1c9ea8acba4f3/classes/lesson_23_Class_and_Exemplars.py
# Классы и экземпляры, наследование

class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def description_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()

    def read_odometr(self):
        """Выводим пробег авто"""
        print("Пробег %s %s %s" % (self.make, self.model, self.year) + " года выпуска: " + str(self.odometr) + " км")

    def update_odometr(self, km):
        """Устанавливает пробег"""
        if km >= self.odometr:
            self.odometr = km
        else:
            print("Это автомобиль, а не машина времени")

    def increment_odometr(self, km):
        """Увеличиваем пробег на заданную величину"""
        if km >= self.odometr:
            self.odometr += km
        else:
            print('Не скручивай!')

class Battery():
    """Just accumulator model for ElectricCar"""

    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        """Выводит инфо об уровне баттареи"""
        print("Этот автомобиль имеет аккумулятор мощностью " + str(self.battery) + " MAph")

class ElectricCar(Car):
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def description_battery(self):
        """Выводит инфо об уровне баттареи"""
        print("%s %s %s" % (self.make, self.model, self.year) + " имеет аккумулятор мощностью: " + str(self.battery) + " MAph")

    def description_name(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()


if __name__ == "__main__":
    tesla = ElectricCar('tesla', 's', 2018)
    tesla.battery.description_battery()
    tesla.description_battery()

    audi = Car('audi', 'a4', 2017)
    subaru = Car('subaru', 'impreza', 2009)

    audi.update_odometr(0)
    audi.increment_odometr(0)
    audi.read_odometr()

    subaru.update_odometr(5)
    subaru.increment_odometr(12)
    subaru.read_odometr()

# Мой код Задание 9. Миссия невыполнима: Красный портфель
def TheRabbitsFoot(s, encode):
    try:
        assert type(s) is str and s != ''  # Проверяем строку s
        assert type(encode) is bool   # Проверяем слово subs
    
        def delWS(s):  # Удалить пробелы и вернуть строку
            # SS = list(s)
            b = s.split()  
            b = "".join(b)
            return b
        
        def StCol(s):   # Подсчет St и Col для Coder
            s = delWS(s) # Извлекаем строку без пробелов
            N = len(s)  # Длина строки
            NN = pow(N, 0.5)  # Кв.корень
            St = int(NN) # Строка и нижняя границв
            Col = int(NN if (NN - int(NN)) == 0 else NN + 1) # Столбец и верхняя граница
            St = St if (St * Col) >= N else (St + 1) # Увеличиваем число строк, если произведение меньше N
            
            if len(s) < (St * Col):  # Добавляем пробелы в последнюю строку, если элементов не хватает
                n = (St * Col) - len(s)
                for i in range(n):
                    s += ' '
            return s, St, Col
 
        def arr(s, St, Col):   # Создаем матрицу NxM (St x Col) для шифровщика
            SS = list(s) 
            ARR = []
            pos = 0
            for i in range(St):
                b = SS[pos:(pos + Col)]
                ARR.append(b)
                pos += Col
            return ARR
        
        def arr2(s):  # Создаем матрицу для дешифровщика
            SS = list(s)
            ARR = []
            pos = 0
            j = 0
            for i in range(len(SS)):
                if SS[i] == ' ' or (i == len(SS) - 1) :
                    if SS[i] == ' ':
                        b = SS[pos:i]
                    else:
                        b = SS[pos:(i + 1)]
                    ARR.append(b)
                    pos += len(b) + 1
                    assert len(ARR[j]) == len(ARR[0]) or len(ARR[j]) + 1 == len(ARR[0])   
                    if len(ARR[j]) != len(ARR[0]):
                        ARR[j].append(' ')
                    j += 1
            St = len(ARR)
            Col = len(ARR[0])
            return ARR, St, Col

        def Shifr(s, St, Col): # Транспортируем матрицу
            arrTrans = []
            for j in range(Col):
                new_St = []
                for i in range(St):
                    new_St.append(s[i][j])
                arrTrans.append(new_St)
            return arrTrans

        def Coder(s):
            s, St, Col = StCol(s)
            s = arr(s, St, Col)
            arrTrans = Shifr(s, St, Col)
            shifr = []
            for i in range(len(arrTrans)): # Формируем шифр - строку с пробелами
                j = len(arrTrans[i])
                if arrTrans[i][j-1] != ' ':
                    arrTrans[i].append(' ')
                if i == (len(arrTrans) - 1) and arrTrans[i][j-1] == ' ':
                    del arrTrans[i][j-1]
                shifr += arrTrans[i]
            SHIFR = "".join(shifr)
            return SHIFR

        def deCoder(s):
            s, St, Col = arr2(s)
            arrTrans = Shifr(s, St, Col)
            shifr = []
            for i in range(len(arrTrans)): 
                shifr += arrTrans[i]
            SHIFR = delWS("".join(shifr))
            return SHIFR

        if encode == True:
            return(Coder(s))
        else:
            assert "  " not in s  # Проверяем, что в строке не более 1 пробела
            return(deCoder(s))
    
    except AssertionError:
        pass

print(TheRabbitsFoot('отдай мою кроличью лапку', True))
print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))
