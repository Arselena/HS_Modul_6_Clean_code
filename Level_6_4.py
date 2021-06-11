# 6.4. Найдите 12 примеров имён в вашем коде, которые следует избегать, исправьте, и выложите на гитхаб в формате "было - стало" (с учётом контекста).
# 1. Строка 55. Sqares2 -> Square_column(столбцы квадрата)
# 2. Строка 97. t1 -> previous_time
# 3. Строка 113. max -> CentrElement_val
# 4. Строка 114. ii -> CentrElement_id
# 5. Строка 130. Tele2 -> удалено 
# 6. Строка 154. SUM -> daily_summary
# 7. Строка 171. ARR -> TonerConsumption_ASCII
# 8. Строка 189.  sum-> TonerConsumption_SUM
# 9. Строка 205. MAX - > votes_max 
# 10. Строка 206. j -> candidate_num
# 11. Строка 214. SUM -> votes_sum
# 12. Строка 219. j -> candidate_max_votes; Строка 222. res -> result_of_voting;

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
        Squares = []
        for X in range(1, N+1):
            Square_column = []
            for Y in range(1, M+1):
                Square_column.append(0)
            Squares.append(Square_column)

        # Запускаем десант. Если длина массива нечетна, то уменьшаем ее на 1
        if len(battalion) % 2 == 0:
            L = len(battalion)
        else:
            L = len(battalion) - 1
        for i in range(0, L, 2):
            assert battalion[i] <= N  # Проверяем, чтобы координаты десанта попадали в Государство Квадратов
            assert battalion[i+1] <= M  # Проверяем, чтобы координаты десанта попадали в Государство Квадратов
            Squares[battalion[i]-1][battalion[i+1]-1] = 2

        # Захват территории Государства Квадратов
        ZahvatAll = False  # вся территория захвачена
        Dey = 1
        Squares, ZahvatAll = ItogZahvat(Squares)
        while ZahvatAll == False:
            for X in range(N):
                for Y in range(M):
                    if Squares[X][Y] == 2:
                        Squares = zahvat(Squares, X, Y)
                        Squares[X][Y] == 3  # Десантник, который отработал больше не захватывает территорию
            Squares, ZahvatAll = ItogZahvat(Squares)
            Dey += 1

        return Dey
    except AssertionError: 
        pass # Ничего не делать

# 2. Поездка на мотоцикле
def odometer(oksana):
    try:
        assert len(oksana) >= 2 # Проверяем, что длина массива >=2

        # Если длина массива нечетна, то уменьшаем ее на 1. Т.е. считаем, что с последней скоростью мотоциклист не перемещался
        if len(oksana) % 2 == 0:
            N = len(oksana)
        else:
            N = len(oksana) - 1
     
        S = 0  # Расстояние
        previous_time = 0  # Предыдущее время с начала поездки
        for i in range(1, N, 2):
            assert type(oksana[i]) is int and type(oksana[0] ) is int # Проверяем целое ли число в массиве
            assert oksana[i] >= 0 and oksana[0] >= 0 # Проверяем положительное ли число в массиве
            assert (oksana[i] - previous_time) > 0 # Проверяем, что пред.время меньше текущего
            
            S += (oksana[i-1]) * (oksana[i] - previous_time) # скорость * время поездки с этой скоростью
            previous_time = oksana[i] # Запоминаем пред.время
        return S
    except AssertionError: 
        pass # Ничего не делать

# 4. Безумный Макс
def MadMax(N, Tele):
    try:
        def Max(Mas):
            CentrElement_val = Mas[0]
            CentrElement_id = 0
            for i in range(len(Mas)):    
                if Mas[i] > CentrElement_val:
                    CentrElement_val = Mas[i]
                    CentrElement_id = i
            return CentrElement_val, CentrElement_id

        assert type(N) is int and N > 0 and N % 2 == 1 and N <= 127  # Проверяем число N (целое, положительное, нечетное)
        assert len(Tele) == N  # Проверяем, что длина массива = N
        for i in range(len(Tele)):  
            assert type(Tele[i]) is int and Tele[i] >= 0 and Tele[i] <= 255 # Проверяем Элемент массива (целое, положительное) 
        for i in range(len(Tele)):  # Проверяем, что массив -- неповторяющиеся цифры
            for j in range(i+1, len(Tele)):
                assert Tele[i] != Tele[j]
 
        Impuls = []
        
        for i in range((N + 1) // 2):  # Заполняем правую часть по убыванию
            CentrElement_val, CentrElement_id = Max(Tele)
            Impuls.append(CentrElement_val)
            del Tele[CentrElement_id]

        for i in range((N - 1) // 2):  # Заполняем левую часть по возрастанию
            CentrElement_val, CentrElement_id = Max(Tele)
            Impuls.insert(0,CentrElement_val)
            del Tele[CentrElement_id]

        return Impuls
    except AssertionError: 
        pass # Ничего не делать

# 8. Искусственный интеллект для Оксаны
def SumOfThe(N, DATA):
    try:
        assert type(N) is int and N >= 2 and N == len(DATA)
        for i in range(len(DATA)):  
            assert type(DATA[i]) is int  # Проверяем Элемент массива 

        for i in range(1, N):
            if DATA[0] == sum(DATA[1:N]):
                daily_summary = DATA[0]
                break
            elif DATA[N-1] == sum(DATA[0:(N-1)]):
                daily_summary = DATA[N-1]
            else: 
                DATA[0], DATA[i] = DATA[i], DATA[0]
        return daily_summary
    
    except AssertionError:
        pass

# 10. Экономим тонер
def PrintingCosts(Line):
    try:
        assert type(Line) is str

        def ton(simbol):
            TonerConsumpti0on_ASCII = [[' ', 0], ['!', 9], ['"', 6], ['#', 24], ['$', 29], ['%', 22], ['&', 24], ["'", 3], ['(', 12], [')', 12],
                ['*', 17],['+', 13], [',', 7], ['-', 7], ['.', 4], ['/', 10], ['0', 22], ['1', 19], ['2', 22], ['3', 23],
                ['4', 21], ['5', 27], ['6', 26], ['7', 16], ['8', 23], ['9', 26], [':', 8], [';', 11], ['<', 10], ['=', 14],
                ['>', 10], ['?', 15], ['@', 32], ['A', 24], ['B', 29], ['C', 20], ['D', 26], ['E', 26], ['F', 20], ['G', 25],
                ['H', 25], ['I', 18], ['J', 18], ['K', 21], ['L', 16], ['M', 28], ['N', 25], ['O', 26], ['P', 23], ['Q', 31],
                ['R', 28], ['S', 25], ['T', 16], ['U', 23], ['V', 19], ['W', 26], ['X', 18], ['Y', 14], ['Z', 22], ['[', 18],
                ["\\", 10], [']', 18], ['^', 7], ['_', 8], ["`", 3], ['a', 23], ['b', 25], ['c', 17], ['d', 25], ['e', 23], 
                ['f', 18], ['g', 30], ['h', 21], ['i', 15], ['j', 20], ['k', 21], ['l', 16], ['m', 22], ['n', 18], ['o', 20],
                ['p', 25], ['q', 25], ['r', 13], ['s', 21], ['t', 17], ['u', 17], ['v', 13], ['w', 19], ['x', 13], ['y', 24],
                ['z', 19], ['{', 18], ['|', 12], ['}', 18], ['~', 9]]
            
            for i in range(len(TonerConsumption_ASCII)):
                if simbol == TonerConsumption_ASCII[i][0]:
                    cons = TonerConsumption_ASCII[i][1]  # расход
                    return cons
            return 23

        TonerConsumption_ASCII = list(Line)
        TonerConsumption_SUM = 0
        for i in range(len(TonerConsumption_ASCII)):
            TonerConsumption_SUM += ton(TonerConsumption_ASCII[i])
    
        return TonerConsumption_SUM
    except AssertionError:
        pass

# 12. 146%
def MassVote(N, Votes):
    try:
        assert type(N) is int and N >=1 and N == len(Votes)
        for i in range(len(Votes)):  
            assert type(Votes[i]) is int and Votes[i] >= 0 # Проверяем Элемент массива (целое, положительное) 

        def max(s):  # Возвращает инднкс наибольшего эл-та массива
            votes_max = s[0]
            candidate_num = 0
            for i in range(1, len(s)):
                if votes_max < s[i]:
                    votes_max = s[i]
                    candidate_num = i
            return candidate_num

        def sum(s):
            votes_sum = 0
            for i in range(len(s)):
                votes_sum += s[i]
            return votes_sum

        candidate_max_votes = max(Votes)
        for i in range(len(Votes)):
            if candidate_max_votes != i and Votes[i] == Votes[candidate_max_votes]:
                result_of_voting = 'no winner'
                return result_of_voting
        
        if Votes[candidate_max_votes] * 100 / sum(Votes) > 50:
            result_of_voting = 'majority winner ' + str(candidate_max_votes + 1)
        else:
            result_of_voting = 'minority winner ' + str(candidate_max_votes + 1)

        return result_of_voting
    except AssertionError:
        pass