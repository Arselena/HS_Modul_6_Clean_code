# "Ясный стиль". Задание 6.4. Найдите пять имён переменных в своём коде, длины которых не укладываются в 8-20 символов, и исправьте, чтобы они укладывались в данный диапазон.
# 1. Строка 20. b –> string_without_spaces
# 2. Строка 25. N -> size_string
# 3. Строка 26. NN -> sqrt_size_string
# 4. Строка 39. ARR –> array_for_encode
# 5. Строка 49. ARR -> array_for_decode
# 6. Строка 82. SHIFR -> encoded_string
# 7. Строка 96. SHIFR -> decoded_string


# 9. Миссия невыполнима: Красный портфель
# Функция string TheRabbitsFoot(string s, bool encode)
# получает исходную строку s и либо зашифровывает её (encode = true), либо расшифровывает (encode = false), только конечно без исходных пробелов.

def TheRabbitsFoot(s, encode):
    try:
        assert type(s) is str and s != ''  # Проверяем строку s
        assert type(encode) is bool   # Проверяем слово subs
    
        def delWS(s):  # Удалить пробелы и вернуть строку
            string_without_spaces = s.split()  
            string_without_spaces = "".join(string_without_spaces)
            return string_without_spaces
        
        def StCol(s):   # Подсчет St и Col для Coder
            s = delWS(s) # Извлекаем строку без пробелов
            size_string = len(s)  # Длина строки
            sqrt_size_string = pow(size_string, 0.5)  # Кв.корень
            St = int(sqrt_size_string) # Строка и нижняя границв
            Col = int(sqrt_size_string if (sqrt_size_string - St) == 0 else sqrt_size_string + 1) # Столбец и верхняя граница
            St = St if (St * Col) >= size_string else (St + 1) # Увеличиваем число строк, если произведение меньше N
            
            if len(s) < (St * Col):  # Добавляем пробелы в последнюю строку, если элементов не хватает
                n = (St * Col) - len(s)
                for i in range(n):
                    s += ' '
            return s, St, Col
 
        def arr(s, St, Col):   # Создаем матрицу NxM (St x Col) для шифровщика
            SS = list(s) 
            array_for_encode = []
            pos = 0
            for i in range(St):
                b = SS[pos:(pos + Col)]
                array_for_encode.append(b)
                pos += Col
            return array_for_encode
        
        def arr2(s):  # Создаем матрицу для дешифровщика
            SS = list(s)
            array_for_decode = []
            pos = 0
            j = 0
            for i in range(len(SS)):
                if SS[i] == ' ' or (i == len(SS) - 1) :
                    if SS[i] == ' ':
                        b = SS[pos:i]
                    else:
                        b = SS[pos:(i + 1)]
                    array_for_decode.append(b)
                    pos += len(b) + 1
                    assert len(array_for_decode[j]) == len(array_for_decode[0]) or len(array_for_decode[j]) + 1 == len(array_for_decode[0])   
                    if len(array_for_decode[j]) != len(array_for_decode[0]):
                        array_for_decode[j].append(' ')
                    j += 1
            St = len(array_for_decode)
            Col = len(array_for_decode[0])
            return array_for_decode, St, Col

        def Shifr(s, St, Col): # Транспортируем матрицу
            arrTrans = []
            for j in range(Col):
                tmp2 = []
                for i in range(St):
                    tmp2.append(s[i][j])
                arrTrans.append(tmp2)
            return arrTrans

        def enCode(s):
            s, St, Col = StCol(s)
            s = arr(s, St, Col)
            arrTrans = Shifr(s, St, Col)
            encoded_string = []
            for i in range(len(arrTrans)): # Формируем шифр - строку с пробелами
                j = len(arrTrans[i])
                if arrTrans[i][j-1] != ' ':
                    arrTrans[i].append(' ')
                if i == (len(arrTrans) - 1) and arrTrans[i][j-1] == ' ':
                    del arrTrans[i][j-1]
                encoded_string += arrTrans[i]
            encoded_string = "".join(encoded_string)
            return encoded_string

        def deCode(s):
            s, St, Col = arr2(s)
            arrTrans = Shifr(s, St, Col)
            decoded_string = []
            for i in range(len(arrTrans)): 
                decoded_string += arrTrans[i]
            decoded_string = delWS("".join(decoded_string))
            return decoded_string

        if encode == True:
            return(enCode(s))
        else:
            assert "  " not in s  # Проверяем, что в строке не более 1 пробела
            return(deCode(s))
    
    except AssertionError:
        pass

print(TheRabbitsFoot('отдай мою кроличью лапку', True))
print(TheRabbitsFoot('омоюу толл дюиа акчп йрьк', False))