# 7.4. Попробуйте найти в своих решениях два-три случая, когда можно использовать пары имён - антонимы.
# Строка 32. begin/end - начало/конец строки

# 7. Конкурент Google
def WordSearch(len1, s, subs):
    try:
        assert type(len1) is int and len1 > 0  # Проверяем число N (целое, положительное)
        assert type(s) is str and len(s) > 0   # Проверяем строку s
        assert type(subs) is str and 0 < len(subs) <= len(s)   # Проверяем слово subs
        assert "  " not in s  # Проверяем, что в строке не более 1 пробела

        def STROne(S, begin, end):  # Формирование одной строки  
            if (end + 1) < len(S) and S[end + 1] != ' ':
                for i in range(end, begin-1, -1):
                    tmp = S[i]
                    if S[i] == ' ':
                        end = i
                        strOne = "".join(S[begin:(end+1)])
                        break
                    elif i == begin:
                        strOne = "".join(S[begin:(end+1)])
            else:
                strOne = "".join(S[begin:(end+1)])
            return strOne, end

        def arrWords(len1, S):  # Формирование массива из строк заданной ширины
            SS = list(S)
            end = -1
            strWords = []
 
            while end+1 != len(S):
                begin = end + 1
                if S[begin] == ' ': # Удаляем пробел вначале
                    begin += 1
                if begin == 0: # Для первого элемента
                    end = len1 - 1
                elif (end + len1) >= len(S): # для последнего элемента
                    end = len(S) - 1
                else:
                    end = begin + len1 - 1 # Для всех остальных эл-ов
                
                S1, end = STROne(SS, begin, end)
                strWords.append(S1)
                print(strWords)
            return(strWords)

    #    def findWord(S, subs):

        if len1 == 1:
            S = s
        elif len1 >= len(s):
            S = [s]
        else:
            S = arrWords(len1, s)
        strRez = []
        
        for i in range(len(S)):
            if subs + ' ' in S[i] or subs == S[i]:
                strRez.append(1)
            else:
                strRez.append(0)
        return(strRez)
    except AssertionError:
        pass

#print(WordSearch(10, '12345', 'subs'))
print(WordSearch(10, '1) stroka razbivaetsya na nabor strok...', 'stroka'))