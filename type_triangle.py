'''
Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов: rectangular для прямоугольного треугольника,
acute для остроугольного треугольника, obtuse для тупоугольного треугольника
или impossible, если треугольника с такими сторонами не существует.
'''
a = int(input())
b = int(input())
c = int(input())

if (a >= b + c) or (b >= a + c) or (c >= b + a):
    print('impossible')
elif (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
    print('rectangular')
elif (a**2 > b**2 + c**2) or (b**2 > a**2 + c**2) or (c**2 > b**2 + a**2):
    print('obtuse')
else:
    print('acute')
