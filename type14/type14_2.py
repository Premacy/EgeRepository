"""Операнды арифметического выражения записаны в системе счисления с основанием 15:
123x5 + 1x233
В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления. 
Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 14.
Для найденного значения x вычислите частное от деления значения арифметического выражения на 14 и укажите его в ответе в 
десятичной системе счисления. Основание системы счисления в ответе указывать не нужно."""


#Внимание. В этом задании требуется определить НАИМЕНЬШЕЕ x  из 15 ричной системы, 
#при котором сумма кратна 14

alph = "123456789ABCDE"
x_min = 15              #за начальное минимальное x берем 15
result = 0

for x in alph:
    a = int("123" + x + "5", 15)
    b = int("1" + x + "233", 15)

    sum = a + b

    if sum % 14 == 0:   #проверка кратности
        if x_min > int(x, 15): #Поиск минимального x, при котором сумма кратна
            result = sum / 14
            x_min = int(x ,15)
print(result)

#ДРУГОЕ РЕШЕНИЕ без использования функции int(x, base_x)

x_min = 15              #за начальное минимальное x берем 15
result = 0

for x in range(0, 15):
    a = 5 + x*15 + 3*15**2 + 2*15**3 + 1*15**4 #по честному переводим из 15 ричной системы в 10
    b = 3 + 3*15 + 2*15**2 + x*15**3 + 1*15**4 #аналогично
    sum = a + b

    if sum % 14 == 0:   #проверка кратности
        if x_min > x: #Поиск минимального x, при котором сумма кратна
            result = sum / 14
            x_min = x
print(result)
