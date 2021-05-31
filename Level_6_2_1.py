# 12. 146%
# Поступил крупный заказ на автоматизацию процесса подсчёта результатов выборов.
# В систему поступает количество голосов, отданных за каждого из кандидатов. Она должна обработать их и определить один из трёх вариантов результата:
# - победитель, набравший больше всех голосов и при этом более 50% голосов;
# - победитель, набравший больше всех голосов и при этом менее или ровно 50% голосов;
# - перевыборы (выявлено несколько победителей с одинаковым количеством голосов).
# "Ясный стиль". Задание 6.1. Изменены переменные строк 16, 17, 25, 30, 31, 34

def MassVote(N, Votes):
    try:
        assert type(N) is int and N >=1 and N == len(Votes)
        for i in range(len(Votes)):  
            assert type(Votes[i]) is int and Votes[i] >= 0 # Проверяем Элемент массива (целое, положительное) 

        def max(s):  # Возвращает номер наибольшего эл-та массива
            number_of_votes = s[0]  # было MAX. Максимальное чисо голосов
            first_candidate_with_the_maximum_number_of_votes = 0 # было j. Номер кандидата с максимальным числом голосов
            for i in range(1, len(s)):
                if number_of_votes < s[i]:
                    number_of_votes = s[i]
                    first_candidate_with_the_maximum_number_of_votes = i
            return first_candidate_with_the_maximum_number_of_votes

        def sum(s):
            total_of_all_votes = 0  # было SUM. Сумма всех голосов
            for i in range(len(s)):
                total_of_all_votes += s[i]
            return total_of_all_votes

        first_candidate_with_the_maximum_number_of_votes = max(Votes) # было j. Перый кандидат с максимальным числом голосов
        for candidate in range(len(Votes)):  # было i. Текущий кандидат 
            if first_candidate_with_the_maximum_number_of_votes != candidate and\
                Votes[candidate] == Votes[first_candidate_with_the_maximum_number_of_votes]:
                result_of_elections = 'no winner'  # было rez. Результат выборов
                return result_of_elections
        
        if Votes[first_candidate_with_the_maximum_number_of_votes] * 100 / sum(Votes) > 50:
            result_of_elections = 'majority winner ' + str(first_candidate_with_the_maximum_number_of_votes + 1)
        else:
            result_of_elections = 'minority winner ' + str(first_candidate_with_the_maximum_number_of_votes + 1)

        return result_of_elections
    
    except AssertionError:
        pass

print(MassVote(7, [5,5,8,9,10,15,15]))