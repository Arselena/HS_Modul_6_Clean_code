# 6.14 Комментарии

# Прокомментируйте 7 мест в своём коде там, где это явно уместно
# 1. Задача 20. Делаем национальный редактор "Лапоть"
# Комментарии уместны, т.к. расшифровывают код операции, указанной в условии задачи
if command[0] == "1":  # Добавить строку
    if be_chang == True:  
        list_chang = list_chang[-1:]
        list_redo = []
    S_current += command[2:]
    list_chang.append(S_current)
    be_chang = False 

# 2. Задача 2. Поездка на мотоцикле
# Комментап=рий уместен, т.к. дает пояснения по сути задачи
def odometer(oksana):
    # Если длина массива нечетна, то уменьшаем ее на 1. Т.е. считаем, что с последней скоростью мотоциклист не перемещался
    if len(oksana) % 2 == 0:
        N = len(oksana)
    else:
        N = len(oksana) - 1

# 3. Задача 10.Экономим тонер
# Комментап=рий уместен, т.к. дает пояснения по сути задачи
# много кода
    for i in range(len(TonerConsumption_ASCII)):
        if simbol == TonerConsumption_ASCII[i][0]:
            cons = TonerConsumption_ASCII[i][1]
            return cons
    return 23  # Если встречается символ, не учитываемый таблицей из документации, то расход = 23

# 4. Задача 14. Оптимизация беспилотного трафикв
# Комментап=рий уместен, т.к. расшифровывают входные данные задания
def Unmanned(L, N, track):  # L - длина дороги
                            # N - кол-во светофоров
                            # track - момент вр. от начала дороги, вр. показа красного света и время показа зелёного цвета

# 5. Задача 20. Делаем национальный редактор "Лапоть"
# Комментап=рий уместен, т.к. расшифровывают входные данные задания
class editor:
    def __init__(self)
        self.S_current = ""  # Текущая строка
        self.list_chang = []  # Список изменений
        self.list_redo = []  # Список для отмены отмены
        self.be_chang = False  # Признак, что были изменения

# 6. Задача 24. Матрица: Вращение
# Комментарии уместны, т.к. с индексами всегда возможна путаница
def MatrixTurn(Matrix:str, M:int, N:int, T:int):
    def rotate(Matrix, i1, i2, j1, j2, Et): # i1, i2, j1, j2 - края 'кольца', Et = Matrix_copy
        if i2+1 // 2 >= len(Matrix) // 2:
            for j in range(j1, j2):
                Matrix[i1][j+1] = Et[i1][j]  # Поворот верхнего края
                Matrix[i2][j] = Et[i2][j+1]  # Поворот нижнего края
            for i in range(i1, i2):
                Matrix[i][j1] = Et[i+1][j1]  # Поворот левого края
                Matrix[i+1][j2] = Et[i][j2]  # Поворот правого края
            rotate(Matrix, i1+1, i2-1, j1+1, j2-1, Et)  # Сужаем кольцо матрицы и снова поворачиваем
# 7. Больше не нашла уместных комментариев (. Комментарии чаще пишу для себя, чтобы запомнить смысл встроенных ф-ий.

# Найдите 5 мест, где эти комментарии были излишни, удалите их и сделайте сам код более наглядным.
# 1. Задача 10. Экономим тонер
# было
def ton(simbol):
    TonerConsumption_ASCII = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22,\
    # много кода 
                                'z': 19, '{': 18, '|': 12, '}': 18, '~': 9}

    if simbol in TonerConsumption_ASCII:
        cons = TonerConsumption_ASCII.get(simbol) # расход
    else:
        cons = 23        
    return cons
# стало. Комментарий #расход удален. Изменено название ф-ии, переменная cons удалена
def toner_consumption(simbol):
    TonerConsumption_ASCII = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22,\
    # много кода 
                                'z': 19, '{': 18, '|': 12, '}': 18, '~': 9}
    if simbol in TonerConsumption_ASCII:
        return TonerConsumption_ASCII.get(simbol)
    else:
        return 23        

# 2. Задача 19. Автоматизация отчётности о продажах
# было
def sum(s_new):  # Складывает одинаковые позиции 
    i = 0
    while i in range(len(s_new) - 1):
        while s_new[i][0] == s_new[i+1][0]: 
            a = int(s_new[i][1]) + int(s_new[i + 1][1])
            s_new[i][1] = str(a)
            del s_new[i + 1]
        i += 1
    return s_new
# стало. Комментарий "# Складывает одинаковые позиции" удален. Ф-ия переименована 
def sum_of_identical_positions(s_new): 
    i = 0
    while i in range(len(s_new) - 1):
        while s_new[i][0] == s_new[i+1][0]: 
            a = int(s_new[i][1]) + int(s_new[i + 1][1])
            s_new[i][1] = str(a)
            del s_new[i + 1]
        i += 1
    return s_new

# 3. Задача 28. Мастер ключей
# было
for i in range(len(tree)):  # Удалить старые ветки
    for j in range(len(tree[i])):
        if tree_new[i][j] != 0:
            tree_new[i][j] = tree[i][j]
        if tree[i][j] >= 3:
            tree_new[i][j] = 0
            if j + 1 < len(tree[i]):
                tree_new[i][j + 1] = 0
            if j - 1 >= 0:
                tree_new[i][j - 1] = 0
            if i + 1 < len(tree):
                tree_new[i + 1][j] = 0
            if i - 1 >= 0:
                tree_new[i - 1][j] = 0
# стало. Комментарий "# Удалить старые ветки" удален. Для удаления старых веток создана ф-ия delete_old_branches(tree)
def delete_old_branches(tree):
    for i in range(len(tree)): 
        for j in range(len(tree[i])):
            if tree_new[i][j] != 0:
                tree_new[i][j] = tree[i][j]
            if tree[i][j] >= 3:
                tree_new[i][j] = 0
                if j + 1 < len(tree[i]):
                    tree_new[i][j + 1] = 0
                if j - 1 >= 0:
                    tree_new[i][j - 1] = 0
                if i + 1 < len(tree):
                    tree_new[i + 1][j] = 0
                if i - 1 >= 0:
                    tree_new[i - 1][j] = 0
    return tree_new

# 4. Задача 4.5. Итераторы
# было
def iterator_2(N, flag):
    l2 = List2(N, flag)   # объект, True = конечно, False = бесконечно
    il2 = iter(l2) # итератор этого объекта
# стало. Комментарии удалены. Переменная flag переименована на finity
def iterator_2(N, finity=True):
    l2 = List2(N, finity)   
    il2 = iter(l2)

# 5. Задача 4.6.1. 
# было
# много кода
def big_sum(s:list, n:int):
    begin = 0
    end = 10000
    step = 10000
    sum_list = []  # список сумм кусочков списка
    t = {}  # словарь процессов
# стало. Комментарии удалены. Переменные sum_list и t переименованы в list_of_sums_of_pieces и dictionary_of_processes
def big_sum(s:list, n:int):
    begin = 0
    end = 10000
    step = 10000
    list_of_sums_of_pieces = [] 
    dictionary_of_processes = {}
