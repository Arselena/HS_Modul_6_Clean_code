# "Ясный стиль". Задание 6.2. Приведите четыре примера, где вы в качестве имён переменных использовали или могли бы использовать технические термины из информатики.
# 1. строка 13 (data - входные данные) 
# 2. строка 29 (octal_or_hex - восьмиричная или шестнадцатеричеая система исчисления)
# 3. строка 51 (remove_words всесто delWS - удалить все пробелы)
# 4. строка 73 (St, Col - строка и столбец)

# 13. Сигналы НЛО
# Функция int [] UFO(int N, int [] data, bool octal)
# получает на вход длину N цифровой записи трафика, сам трафик (последовательность положительных чисел) в массиве data, и флажок octal, который задаёт систему счисления входных данных: восьмеричная если octal = true, и шестнадцатеричная в противном случае.
# Если числа подаются в восьмеричной системе счисления, гарантируется, что в них не будет цифр 8 и 9.
# Функция возвращает массив длины N, содержащий исходные числа, преобразованные в десятичную систему счисления.

def UFO(N, data, octal):
    try:    
        def trans(num, SS):
            arr = list(int(d) for d in str(num))
            n = len(arr)
            sum = 0
            for i in range(n):
                if SS == 8:
                    assert arr[i] < 8  # исключаем цифры 8 и 9 в восьмеричной CC
                sum += arr[i] * (SS ** (n - 1))
                n -= 1
            return sum
        
        assert type(N) is int and N == len(data)
        assert type(octal) is bool
        for d in data:
            assert type(d) is int

        if octal == True:
            octal_or_hex = 8  # восьмиричная или шестнадцатеричеая система исчисления
        else:
            octal_or_hex = 16 
        
        ARR = []
        for d in data:
            ARR.append(trans(d, octal_or_hex))
        
        return ARR
    
    except AssertionError:
        pass

# 9. Миссия невыполнима: Красный портфель
# Функция string TheRabbitsFoot(string s, bool encode)
# получает исходную строку s и либо зашифровывает её (encode = true), либо расшифровывает (encode = false), только конечно без исходных пробелов.
def TheRabbitsFoot(s, encode):
    try:
        assert type(s) is str and s != ''  # Проверяем строку s
        assert type(encode) is bool   # Проверяем слово subs
    
        def delWS(s):  # Удалить пробелы и вернуть строку  # Праивльнее remove_words
            SS = list(s)
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
                tmp2 = []
                for i in range(St):
                    tmp2.append(s[i][j])
                arrTrans.append(tmp2)
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