# 6.10. Переменные и их значения

# 1. Задача 12. 146%
# было
    candidate_max_votes = max(Votes)
    # много кода
    for i in range(len(Votes)):
        if candidate_max_votes != i and Votes[i] == Votes[candidate_max_votes]:
            result_of_voting = 'no winner'
            return result_of_voting
    # много кода
# стало. Инициализация переменной перенесена ближе к первому обращению к ней.
    # много кода
    candidate_max_votes = max(Votes)
    for i in range(len(Votes)):
        if candidate_max_votes != i and Votes[i] == Votes[candidate_max_votes]:
            result_of_voting = 'no winner'
            return result_of_voting
    # много кода

# 2. Задача 4. Безумный Макс
# было без проверки
# стало с проверкой на допустимость значений
    def MadMax(N, Tele):
        # много кода
        try:
            for i in range(len(Tele)):  
                assert type(Tele[i]) is int and Tele[i] >= 0 and Tele[i] <= 255 # Проверяем Элемент массива (целое, положительное) 
            for i in range(len(Tele)):  # Проверяем, что массив -- неповторяющиеся цифры
                for j in range(i+1, len(Tele)):
                    assert Tele[i] != Tele[j]
        except AssertionError:
            ptint("ERROR: элемент массива на соответсвует заданию (целые положительные, не повторяющиеся")

# 3. Задача 3. Освобождение Государства Квадратов 
# было  
    # Захват территории Государства Квадратов
    ZahvatAll = False  
    Dey = 1
    Squares, ZahvatAll = ItogZahvat(Squares)
    while ZahvatAll == False:
        for X in range(N):
            for Y in range(M):
                if Squares[X][Y] == 2:
                    Squares = zahvat(Squares, X, Y)
                    Squares[X][Y] == 3  
        Squares, ZahvatAll = ItogZahvat(Squares)
        Dey += 1
# стало
    # ZahvatAll = False  # дважды инициализировалась
    Squares, ZahvatAll = ItogZahvat(Squares)
    Dey = 1  # счетчик перенесен непосредственно перед циклом
    while ZahvatAll == False:
        for X in range(N):
            for Y in range(M):
                if Squares[X][Y] == 2:
                    Squares = zahvat(Squares, X, Y)
                    Squares[X][Y] == 3  
        Squares, ZahvatAll = ItogZahvat(Squares)
        Dey += 1
# 4. добавим в этот же код завершение работы с переменной    
    Dey = None 

# 5. Задача 6. Разблокировка мобильных телефонов 
# было
    # много кода 
    lock_code_list = [] 
    i = 0
    while i < len(a):
        if sum_of_code_str[i] != '0':
            lock_code_list.append(sum_of_code_str[i])
        i += 1
    lock_code_str = "".join(lock_code_list)
# сталою. Добавим в код завершение работы с переменной
    i = None 

# 6. Задача 8. Искусственный интеллект для Оксаны
# было
    def SumOfThe(N, DATA):
        daily_summary = None 
        # много кода
        for i in range(1, N):
            if DATA[0] == sum(DATA[1:N]):
                daily_summary = DATA[0]  
                break
            elif # много кода
# стало. Инициализация переменной перенесена ближе к первому обращению к ней.
    def SumOfThe(N, DATA):
        # много кода
        daily_summary = None  
        for i in range(1, N):
            if DATA[0] == sum(DATA[1:N]):
                daily_summary = DATA[0]  
                break
            elif # много кода

# 7. Задача 14. Оптимизация беспилотного трафика
# было
    def light(t, r, g):
        k = t % (r + g)
        ost = r - t % (r + g)  
        if (0 < ost <= r):
            pos = 'red' 
        else:
            pos = 'green'       
        return pos, ost
# стало. Удалена неиспользуемая переменная
    def light(t, r, g):
        # k = t % (r + g) # не используется
        ost = r - t % (r + g)  
        if (0 < ost <= r):
            pos = 'red' 
        else:
            pos = 'green'       
        return pos, ost

# 8. Задача 26. Саурон и многомерное Кольцо Всевластья
# было
    pos = 0
    while pos < len(S[j])-1:  # перебираем все правильные последовательности от pos
        for i in range(pos, len(S[j])):  
            if S[j][i] == '(':  
                balance += 1
            else:
                # много кода
# стало. Добавим в код завершение работы с переменной
    pos = None

# 9 и 10. Задача 27.
# было
    index = []
    # много кода  
    for i in range(len(F)):  
        if F[i] != F_sort[i]:
            index.append(i)
    # много кода
    for i in index:  
        if F_rev[index[i]] != F_sort[index[i]]:
            CanOrder = False
            return CanOrder
    return CanOrder
# стало 
    # много кода
    index = [] # 9. Инициализация переменной перенесена ближе к первому обращению к ней.
    for i in range(len(F)):  
        if F[i] != F_sort[i]:
            index.append(i)
    # много кода
    F_rev = ''.join(reversed(F)) # 10. Инициализация переменной перенесена ближе к первому обращению к ней.
    for i in index: 
        if F_rev[index[i]] != F_sort[index[i]]:
            CanOrder = False
            return CanOrder
    return CanOrder

# 11. Задача 15. Танковый раш
# было
    j1 = 0
    while j1 in range(W1): # стролбцы S1
            index_start = S1[i1].find(S2[0], j1)
            if index_start != -1:
                index_end = index_start + W2 
                St_end = i1 + H2
                S1_new = find(S1, i1, St_end, index_start, index_end) 
                
                if S1_new == S2:
                    flag = True
                    break
            j1 += 1
# стало. Добавим в код завершение работы с переменной
    j1 = None

# 12. Задача 18. Мистер Робот и Корпорация Зла
# было
    def shift_left(index, s):
        i = s[index] - 1
        pos = 0
        while index != i or pos > 100:
            if index == len(s) - 1:
                a1, a2, a3 = (index - 2), (index - 1), (index)
                s[a1], s[a2], s[a3] = s[a2], s[a3], s[a1]
            else:
                a1, a2, a3 = (index - 1), index, (index + 1)
                s[a1], s[a2], s[a3] = s[a2], s[a3], s[a1]
            index -= 1
            pos += 1
        return s
# стало. Добавим в код завершение работы с переменной
        pos = None

# 13. Задание 9. Миссия невыполнима: Красный портфель
# было 
    def StCol(s):
        without_spaces_str = delWS(s) 
        # много кода
        if len(without_spaces_str) < (St * Col):  
            n = (St * Col) - len(s)
            for i in range(n):
                without_spaces_str += ' '
        return without_spaces_str, St, Col
# стало. Инициализация переменной перенесена ближе к первому обращению к ней.
    def StCol(s):
        # много кода
        without_spaces_str = delWS(s) 
        if len(without_spaces_str) < (St * Col):  
            n = (St * Col) - len(s)
            for i in range(n):
                without_spaces_str += ' '
        return without_spaces_str, St, Col

# 14. Код взят на https://github.com/SuRRoK/python_lessons/blob/a358ffa8ae3931f17e448b809fc09032d2e0f6c5/lesson_008/python_snippets/01_inheritance.py
# было
    class Pet:
    """ Домашнее животное """
    legs = 4
    has_tail = True

    def __init__(self, name):
        self.name = name
    # много кода
# стало. Инициализируйте все без исключения атрибуты/поля класса в его конструкторе.
    class Pet():
    """ Домашнее животное """
        def __init__(self, name):
            self.name = name
            self.legs = 4
            self.has_tail = True
    # много кода

# 15. Код взят на https://github.com/Motokulman/plan2020/blob/4eeca7f137684048a529dd3d13fa4c44d169df87/standards/models.py
# было
    class Meta:
        ordering = ('name',)
        verbose_name = 'Класс средней плотности'
        verbose_name_plural = 'Классы средней плотности'
# стало. Инициализируйте все без исключения атрибуты/поля класса в его конструкторе.
    class Meta:
        def __init__(self)
            self.ordering = ('name',)
            self.verbose_name = 'Класс средней плотности'
            self.verbose_name_plural = 'Классы средней плотности'
