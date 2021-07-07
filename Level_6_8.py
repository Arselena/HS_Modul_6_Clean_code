# 6.8. Константы
# Внесите 12 правок в свой код, в которых улучшите работу с константами, и напишите по каждой, что конкретно вы улучшили.
# 1. Строки с 26 по 47. Все цифры обозначают кнопки телефона, поэтому добавим константы: было 1,2...9 -> PHONE_BUTTON_1 = 1, PHONE_BUTTON_2 = 2 ... PHONE_BUTTON_9 = 9
# 2. Строка 97. 50 - это 50% всех голосов при подсчете рез-в выборов. Ввести константу HALF_ALL_VOTES_PERCENT = 50; заменить 50 - > HALF_ALL_VOTES_PERCENT
# 3. Было birth_year -> BIRTH_YEAR. Константа заглавными буквами
# 4. Было pi = 3.14 -> PI = 3.14   
# 5. Было pach = r'C:\Users\El\Desktop\Python\Database' -> PATH_TO_DATABASE = r'C:\Users\El\Desktop\Python\Database'
# 6. Строка 112. name1 -> FIRST_FILE_NAME. Имя первого файла
# 7. Строка 118. fi1 -> FILE_1. 
# 8. Было 10 -> FILE_COUNT = 10. Количество файлов, которые необходимо создать
# 9. WELCOME_MESSAGE - приветственной сообщение
# 10. ALPHABET_VOWELS = "AEIOUY"
# 11. ALPHABET_CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
# 12. MAX_VALUE = 3

# 6. Разблокировка мобильных телефонов
def PatternUnlock(N, hits):
    try:
        assert type(N) is int and N > 0 # Проверяем число N (целое, положительное)
        assert N == len(hits)
        for i in range(len(hits)):  
            assert type(hits[i]) is int and  1 <= hits[i] <= 9 # Проверяем Элемент массива (целое, положительное) 
        
        def length(pos, next):hhnhhh.
            leng = 0
            if (pos == 1 and next in (6, 2, 9) or
            pos == 2 and next in (1, 3, 5, 8) or 
            pos == 3 and next in (2, 4, 7) or 
            pos == 4 and next in (3, 5) or
            pos == 5 and next in (2, 4, 6) or
            pos == 6 and next in (1, 5) or
            pos == 7 and next in (3, 8) or
            pos == 8 and next in (2, 7, 9) or
            pos == 9 and next in (1, 8)):
                leng = 1
            
            elif (pos == 1 and next in (5, 8) or
                pos == 2 and next in (4, 6, 7, 9) or 
                pos == 3 and next in (5, 8) or
                pos == 4 and next == 2 or
                pos == 5 and next in (3, 1) or
                pos == 6 and next == 2 or 
                pos == 7 and next == 2 or
                pos == 8 and next in (1, 3) or 
                pos == 9 and next == 2):
                leng = pow(2, 0.5)
            return leng        
            
        # Считаем сумму, 
        sum = 0
        for i in range(N-1):
            sum += length(hits[i], hits[i+1])
        a = list(str(round(sum * pow(10, 5)))) # Округляем и переводим в строку
        
        # Удаляем 0 и преобразуем в строку
        b = []
        i = 0
        while i < len(a):
            if a[i] != '0':
                b.append(a[i])
            i += 1
        S = "".join(b)

        return S
    
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


# 2.8. Работа с файлами.
# Задание 3.2. Напишите программу, которая получает на вход два случайных числа от 1 до 10, по этим числам открывает два соответствующих файла из задания выше, и возвращает сумму шести чисел (содержимое обоих файлов). Обрабатывайте ситуацию, когда содержимое файла неполно или испорчено.
import random

try:
    name1 = str(random.randint(1, 10)) + '.txt'
    # name1 = '1.txt'
    name2 = str(random.randint(1, 10)) + '.txt'
    while name1 == name2:
        name2 = str(random.randint(1, 10)) + '.txt'

    fi1 = open(name1, 'rt')
    fi2 = open(name2, 'rt')
    print(fi1, fi2)

    sum = 0
    for i in range(3):
        s1 = fi1.readline()
        s2 = fi2.readline()
        if s1 == '' and s2 != '': # если строка s1 пустая, то суммируем только s2
            sum += int(s2)
        elif s2 == '' and s1 != '': # если строка s2 пустая, то суммируем только s1
            sum += int(s1)
        else:
            sum += int(s1) + int(s2)
    print(sum)

except ValueError:
    print('Файл испорчен')