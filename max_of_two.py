'''
Напишите программу, которая считывает два целых числа A и B и выводит наибольшее значение из них.
Числа — целые от 1 до 1000.
При решении задачи можно пользоваться только целочисленными арифметическими операциями.
Нельзя пользоваться нелинейными конструкциями: ветвлениями, циклами, функциями.
'''
A = int(input())
B = int(input())

diff = ((A - B)**2)**.5
max_num = int((A + B + diff) // 2)

print(max_num)
