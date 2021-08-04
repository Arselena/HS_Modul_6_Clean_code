# 6.13. Массивы

# 1. Задача 4. Безумный Макс.
# В данной задаче можно использовать структуру "Упорядоченный список". 
# много кода (реализация Упорядоченного списока OrderedList)
def MadMax(N, Tele):
    # упорядочиваем список(массив) Tele по возрастанию
    s_list = OrderedList() 
    for i in range(N):
        s_list.add(Tele[i])  

    # записываем в Impuls первую половину в порядке возрастания
    Impuls = [] 
    node = s_list.head
    for i in range(N//2):
        Impuls.append(node.value)
        node = node.next
    # записываем в Impuls вторую половину в порядке убывания
    node = s_list.tail
    while len(Impuls) < N:
        Impuls.append(node.value)
        node = node.prev
    return Impuls

# 2. Задача 6. Разблокировка мобильных телефонов
# В данной задаче можно использовать структуру "Очередь". 
# много кода (реализация списока LinkedList)
def PatternUnlock(N, hits):
    # ф-ия преобразования списка(мвссива) объект список
    def transformation_in_LinkedList(array):
        s_list = LinkedList()
        for i in range(len(array)):
            s_list.add_in_tail(Node(array[i]))
        return s_list
    
    # Записываем список hits в объект "список"
    s_list = transformation_in_LinkedList(hits)
    # Считаем сумму 
    sum = 0
    node = s_list.head
    while node != None:    
        sum += length(node.value, node.next.value)
        node = node.next.next
    unlock_code = list(str(round(sum * pow(10, 5)))) # Округляем и преобразуем в список
    unlock_code_list = transformation_in_LinkedList(unlock_code)

    # Удаляем 0 и преобразуем в строку
    unlock_code_list.delete(0,True) # удаляем все 0
    unlock_code = [] 

    node = unlock_code_list.head
    for i in range(unlock_code_list.len):
        unlock_code.append(node.value)
        node = node.next
    unlock_code = "".join(unlock_code)
    return unlock_code

# 3. Задача 8. Искусственный интеллект для Оксаны
# В данной задаче можно использовать структуру "Очередь". 
#  много кода (реализация списока LinkedList)
def SumOfThe(N, DATA):
    # ф-ия преобразования списка(мвссива) объект список
    def transformation_in_LinkedList(array):
        s_list = LinkedList()
        for i in range(len(array)):
            s_list.add_in_tail(Node(array[i]))
        return s_list
    # Записываем список DATA в объект "список"
    s_list_DATA = transformation_in_LinkedList(DATA)
    # в классе LinkedList реализован метод суммирующий все значения
    sum_all = s_list_DATA.sum 
    balans = int(sum_all / 2)
    # если balans целое число и это число есть в списке, то balans и есть искомое число  
    if sum_all % 2 == 0 and s_list_DATA.find(balans) != None: 
        return balans
    else:
        return "ERROR"

# 4. Задача 10. Экономим тонер
# В данной задаче можно использовать структуру словарь (первоначально использовался двумерный массив)
def ton(simbol):
    dict = {' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22,\
# много кода 
            'z': 19, '{': 18, '|': 12, '}': 18, '~': 9}

    if simbol in dict:
        cons = dict.get(simbol)
    else:
        cons = 23        
    return cons

def PrintingCosts(Line):
    TonerConsumption_ASCII = list(Line)
    TonerConsumption_SUM = 0
    for i in range(len(TonerConsumption_ASCII)):
        TonerConsumption_SUM += ton(TonerConsumption_ASCII[i])
    return TonerConsumption_SUM

# 5. Задача 16. Шопоголики
# В данной задаче можно использовать структуру "Упорядоченный список". 
# много кода (реализация Упорядоченного списока OrderedList и метода get_head)
def MaximumDiscount(N:int, price:int):
    # ф-ия преобразования списка(мвссива) объект OrderedList отсортированный по убыванию
    def transformation_in_LinkedList(array):
        s_list = OrderedList(False) 
        for i in range(len(array)):
            s_list.add(array[i])
        return s_list
    s_list = transformation_in_LinkedList(price)
    sale = 0
    while s_list.head != None:
        s_list.get_head()
        s_list.get_head()
        if s_list.head != None:
            sale += s_list.head.value
        s_list.get_head()
    return sale