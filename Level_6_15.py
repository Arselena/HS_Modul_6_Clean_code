# 6.15 Правильные комментарии

# ИНФОРМАТИВНЫЕ КОММЕНТАРИИ (пояснения к коду)
# 1. Задача 24. Матрица: Вращение
    def rotate(Matrix, i1, i2, j1, j2, Et): # i1, i2, j1, j2 - края 'кольца', Et = Matrix_copy
        if i2+1 // 2 >= len(Matrix) // 2:
            for j in range(j1, j2):
                Matrix[i1][j+1] = Et[i1][j]  # Поворот верхнего края
                Matrix[i2][j] = Et[i2][j+1]  # Поворот нижнего края
            for i in range(i1, i2):
                Matrix[i][j1] = Et[i+1][j1]  # Поворот левого края
                Matrix[i+1][j2] = Et[i][j2]  # Поворот правого края
            rotate(Matrix, i1+1, i2-1, j1+1, j2-1, Et)  # Сужаем кольцо матрицы и снова поворачиваем
# 2. Задача 3. Освобождение Государства Квадратов
    # Итог баталий. Все захваченные территории стали десантом (1 стали 2). Если есть 0, то не вся территория захвачена
    def ItogZahvat(Sq):
        ZahvatAll = True
        for x in range(N):
            for y in range(M):
                if Sq[x][y] == 1:
                    Sq[x][y] = 2
                elif Sq[x][y] == 0:
                    ZahvatAll = False
        return Sq, ZahvatAll

# ПРЕДСТАВЛЕНИЕ НАМЕРЕНИЙ
# 3. Задача 3. Освобождение Государства Квадратов 
    # Запускаем десант
    if len(battalion) % 2 == 0:
        L = len(battalion)
    else:
        L = len(battalion) - 1
    for i in range(0, L, 2):
        assert battalion[i] <= N  
        assert battalion[i+1] <= M 
        Squares[battalion[i]-1][battalion[i+1]-1] = 2

# 4. Задача 5.6. Двусторонняя очередь. Тест
# проверим методы removeFront()
def test_3(self):  
        # удаление из пустого списка
        res11 = self.deq_1.removeFront()
        self.assertEqual(res11, None)
        res_s = self.deq_1.size()
        self.assertEqual(res_s, 0)

# ПРОЯСНЕНИЕ
# 5. Задача 20. Делаем национальный редактор "Лапоть"
# Комментарии расшифровывают код операции, указанной в условии задачи
    if command[0] == "1":  # Добавить строку
        if be_chang == True:  
            list_chang = list_chang[-1:]
            list_redo = []
        S_current += command[2:]
        list_chang.append(S_current)
        be_chang = False 

# 6. Задача 10.Экономим тонер
# Комментарий расшифровывает значение 23, заложенное в условие задачи. Можно сделать константу NO_SIMBOL = 23, и комментарии написать к константе.
    for i in range(len(TonerConsumption_ASCII)):
        if simbol == TonerConsumption_ASCII[i][0]:
            cons = TonerConsumption_ASCII[i][1]
            return cons
    return 23  # Если встречается символ, не учитываемый таблицей из документации, то расход = 23

# 7. Задача 14. Оптимизация беспилотного трафикв
# Комментарий расшифровывают входные данные задания
    def Unmanned(L, N, track):  # L - длина дороги
                                # N - кол-во светофоров
                                # track - момент вр. от начала дороги, вр. показа красного света и время показа зелёного цвета

# 8. Задача 20. Делаем национальный редактор "Лапоть"
# Комментарий расшифровывают входные данные задания
    class editor:
        def __init__(self)
            self.S_current = ""  # Текущая строка
            self.list_chang = []  # Список изменений
            self.list_redo = []  # Список для отмены отмены
            self.be_chang = False  # Признак, что были изменения

# 9. Задача из модуля 4.10. Сервер
    except (ConnectionResetError, ConnectionAbortedError) as e:  # Ловим ошибку когда клиент вышел из чата не по exit
        
# ПРЕДУПРЕЖДЕНИЯ О ПОСЛЕДСТВИЯХ
# 10. Задание 4.1. Связанный (связный) список

# При присутствии исполняемого кода задание не пройдет тест!
# print(max_S([2, 8, 6, 6, 3, 1, 5]))
# print(degree(3, 3))

# УСИЛЕНИЕ
# 11. Задача 5.9 Ассоциативный массив
class NativeDictionary:
    def hash_fun(self, key): # в качестве key поступают строки! всегда возвращает корректный индекс слота!
        if self.size == 0:
            return None
        b = key.encode("utf-8") 
        sum_b = 0
        for i in range(len(b)):
            sum_b += b[i]
        return sum_b % self.size 

# КОММЕНТАРИИ TODO
# 12. 5.4. Стек. Комментарий в методе pop был удален, когда метод был описан
class Stack:
    def pop(self):
        # ваш код
        return None 