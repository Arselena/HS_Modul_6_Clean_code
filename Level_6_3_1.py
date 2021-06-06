# 7.1. Приведите пять примеров правильного именования булевых переменных в вашем коде в формате "было - стало".
# 1. Строка 23. flag -> str2_in_str1
# 2. Строка 45. flag -> text_is_correct
# 3. Строка 64. flag -> valid
# 4. Строка 99. ничего не было -> CanOrder
# 5. Строка 64. flag -> ZahvatAll

# 15. Танковый раш. Поиск подстроки S2 в строке S1
def TankRush(H1, W1, S1, H2, W2, S2):
    
    # Вырезаем список H2 x W2 из S1
    def find(S1, St_start, St_end, Col_start, Col_end):
        S1_new = S1[St_start:St_end]
        for i1 in range(len(S1_new)):
            S1_new[i1] = S1_new[i1][Col_start:Col_end]
        return S1_new

    # Разбиваем строки на подстроки по пробелу
    S1 = S1.split()  
    S2 = S2.split()

    # Ищем подстроку S2[0] во всех строках карты S1
    str2_in_str1 = False
    for i1 in range((H1 - H2) + 1): # строки S1
        index_end = 0
        j1 = 0
        while j1 in range(W1): # стролбцы S1
            index_start = S1[i1].find(S2[0], j1)
            if index_start != -1:
                index_end = index_start + W2
                St_end = i1 + H2
                S1_new = find(S1, i1, St_end, index_start, index_end) 
                
                if S1_new == S2:
                    str2_in_str1 = True
                    break
            j1 += 1            
    return str2_in_str1

# 17. Машинное распознавание паттернов
def LineAnalysis(line:str):
    n = len(line)
    line = line[1:n-1]
    line = line.split('*')
    text_is_correct = True
    if len(line) >= 2:
        for i in range(len(line) - 1):
            if line[i] != line[i + 1]:
                text_is_correct = False
                break
    return text_is_correct

# 22. Шерлок Холмс и механическая шкатулка. Возвращает true, если строка валидна.
def SherlockValidString(s:str):
    s_list = list(s)
    unique = set(s_list)  # Уникальные элементы в строке
    count_list = []
    for i in unique:  # Кол-во уникальных элементов
        n = s_list.count(i)
        count_list.append(n)
    count_list.sort()
    unique2 = list(set(count_list))  # Уникальные кол-ва встречаемых элементов

    valid = False
    # если все эл-ы встречаются по 1 разу
    if (len(unique2) == 1 or 
       # один отличается от остальных и кол-во этого одного = 1
        len(unique2) == 2 and count_list.count(1) == 1 or
       # один отличается от остальных и его кол-во больше на 1 
        len(unique2) == 2 and count_list.count(count_list[-1]) == 1 and (count_list[-1] == count_list[-2] + 1)):
       valid = True
    return valid

# 27. Тренируем сборную России по футболу.Возврещает True, если массив можно упорядочить однократным применением одного из двух правил.
def Football(F, N:int):
    F = list(F)
    F_sort = sorted(F)
    F_rev = ''.join(reversed(F))    
    index = []
    
    CanOrder = True
    if F == F_sort:  # Если массив изначально отсортирован
        CanOrder = False
        return CanOrder
    
    for i in range(len(F)):  # Запишем индексы значений не на своих местах
        if F[i] != F_sort[i]:
            index.append(i)

    if len(index) == 2:  # если не совпали два значения
        return CanOrder
    elif index not in list(range(index[0], (index[0] + len(index) + 1))): # если не совпадения идут не по порядку
        CanOrder = False
        return CanOrder
    
    for i in index:  # eсли развернутый массив совпадает с отсортированным в диапазоне индексов не на своем месте
        if F_rev[index[i]] != F_sort[index[i]]:
            CanOrder = False
            return CanOrder
    return CanOrder

# 3. Освобождение Государства Квадратов 
    def ConquestCampaign(N, M, L, battalion):
    try:
        # Захват территории одним десантником
        def zahvat(Sq, x, y):  
            if (x - 1) >= 0 and Sq[x-1][y] == 0:
                Sq[x-1][y] = 1
            
            if (x + 1) < N and Sq[x+1][y] == 0:
                Sq[x+1][y] = 1 

            if (y - 1) >= 0 and Sq[x][y-1] == 0:
                Sq[x][y-1] = 1

            if (y + 1) < M and Sq[x][y+1] == 0:
                Sq[x][y+1] = 1
            return(Sq)

        # Итог баталий. Все захваченные территории стали десантом (1 стали 2). Если есть 0, то не вся территория захвачена (Flag = False)
        def ItogZahvat(Sq):
            ZahvatAll = True
            for x in range(N):
                for y in range(M):
                    if Sq[x][y] == 1:
                        Sq[x][y] = 2
                    elif Sq[x][y] == 0:
                        ZahvatAll = False
            return Sq, ZahvatAll

        assert type(N) is int and type(M) is int and type(L) is int  # Проверяем целое ли числа
        assert N > 0 and N > 0 and L > 0 # Проверяем положительное ли число в массиве
        for i in range(len(battalion)):  # Проверяем десанта
            assert type(battalion[i]) is int and battalion[i] >= 0 
        assert len(battalion) == L*2 # Проверяем, что у всех десантников есть координаты

        # Заполняем массив Государства Квадратов                 
        Sqares = []
        for X in range(1, N+1):
            Sqares2 = []
            for Y in range(1, M+1):
                Sqares2.append(0)
            Sqares.append(Sqares2)

        # Запускаем десант. Если длина массива нечетна, то уменьшаем ее на 1
        if len(battalion) % 2 == 0:
            L = len(battalion)
        else:
            L = len(battalion) - 1
        for i in range(0, L, 2):
            assert battalion[i] <= N  # Проверяем, чтобы координаты десанта попадали в Государство Квадратов
            assert battalion[i+1] <= M  # Проверяем, чтобы координаты десанта попадали в Государство Квадратов
            Sqares[battalion[i]-1][battalion[i+1]-1] = 2

        # Захват территории Государства Квадратов
        ZahvatAll = False  # вся территория захвачена
        Dey = 1
        Sqares, ZahvatAll = ItogZahvat(Sqares)
        while ZahvatAll == False:
            for X in range(N):
                for Y in range(M):
                    if Sqares[X][Y] == 2:
                        Sqares = zahvat(Sqares, X, Y)
                        Sqares[X][Y] == 3  # Десантник, который отработал больше не захватывает территорию
            Sqares, ZahvatAll = ItogZahvat(Sqares)
            Dey += 1

        return Dey
    except AssertionError: 
        pass # Ничего не делать