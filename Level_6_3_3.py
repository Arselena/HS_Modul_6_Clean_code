# 7.3. Попробуйте найти случай, когда вместо i j k нагляднее использовать более выразительное имя.
# Строка 62. Вместо i, j тспользуется X, Y, т.к. по смыслу это координаты 

# 3. Освобождение Государства Квадратов.
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
        ZahvatAll = False
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