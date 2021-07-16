# 6.9. Типы данных.
# 1. Целые числа
# Проверяйте целочисленность операций деления (используйте подходящие операции деления).
print(7//3) # 2
print(-7//3) # -3;   т.к. 3 * (-3) + 2 
print(7//-3) # -3
print(-7//-3) # 2 
print(" ")
print(7 % 3) # 1
print(-7 % 3) # 2;  Знак делителя и остатка совпалает
print(7 % -3) # -2;  Знак делителя и остатка совпалает
print(-562 % 10) # 8;   
print(10 - (-562 % 10)) # 2;   # Т.е. чтобы получить последнюю цифру отрицательного числа A надо 10 - (A % 10) 

# Проверяйте возможное переполнение целых чисел.
# Переполнение в Pythn возможно при использовании библиотек pydata/numpy/pandas/sys
import numpy as np
a = np.array([3095693933], dtype=int)  
s = np.sum(a)
print(s) # 3095693933
s * s  # -8863423146896543127
print(type(s)) # numpy.int64
py_s = int(s)
print(py_s * py_s) # 9583320926813008489

# 2.Вещественные числа
# Избегайте сравнений на равенство
NORMAL = 1.0
sum = 0
for i in range(11):
    sum = sum + 0.1
print(NORMAL, sum) # NRMAL и sum при сравнении не будут равны 1.0 != 0.9999999999999999

# Предупреждайте и учитывайте ошибки округления.
# Измените тип вещественной переменной на тип с большей точностью.
# Встроенный Python float тип имеет двойную точность, чтобы повысить точнисть можно использовать модуль decimal
from decimal import Decimal    
Decimal(2.675)
Decimal('2.67499999999999982236431605997495353221893310546875') 

# для некоторых приложений, можено использовать Fraction вместо чисел с плавающей точкой.
from fractions import Fraction
Fraction(1, 3)  # числитель, значенатель

# Измените в коде места, где используются значения с плавающей запятой, на целые значения, если это возможно.
# разделить переменные: для целой части и для дробной и обрабатывать их отдельно, например 
dollar = input('введите $:')
cent = input('введите cent:')

# 3. Строки
# Избегайте магических символов и строк -- используйте константы.
HALF_ALL_VOTES_PERCENT = 50 # константа для 50% голосов при подсчете рез-в выборов

# Узнайте, как ваш язык и система поддерживают Unicode, и перейдите на этот формат.
# Методы encode и decode Python используются для кодирования и декодирования входной строки с использованием заданной кодировки
sock_user.send(('Для выхода нажмите exit\n').encode('utf-8')) # Отправляем сообщение для клиентов в закодированном 
data_user_decod = data_user.decode('utf-8')  # получаем информацию от клиентов

# Разработайте стратегию интернационализации/локализации текстовых сообщений в вашем коде (делайте это в самый ранний период создания программы).
# Модуль gettext обеспечивает интернационализацию (I18N) и локализация (L10N) службы для ваших модулей Python и приложений. 
gettext.gettext(Сообщение) # Возвращает локализованный перевод сообщенияна основе текущего глобального каталога домена, языка и языкового региона.

# 4. Логические переменные
# Активнее используйте логические переменные для повышения читабельности программы.
# 28.	Мастер ключей. Изменены 0 и 1 на True и False
def Keymaker(k:int):  # k - кол-во дверей
    def open_close(Close_dors, step):
        for i in range(step-1, len(Close_dors), step): # меняем положение дверей от n-1 с шагом n
            if Close_dors[i] == False:
                Close_dors[i] = True
            else:
                Close_dors[i] = False
        return Close_dors

    Close_dors = [True] * k # массив закрытых дверей
    for i in range(1, k+1):
        if i == 1:
            Close_dors = [False] * k  # открываем все двери
        else:
            Close_dors = open_close(Close_dors, i)
    
    Close_dors = list(map(str, Close_dors))
    Close_dors = ''.join(Close_dors)
    
    return Close_dors