'''
Даны координаты двух точек на плоскости, требуется определить,
лежат ли они в одной координатной четверти или нет (все координаты отличны от нуля).
'''
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

status = True

if x1 > 0:
    if y1 < 0:
        status = False
else:
    if y1 > 0:
        status = False

if x2 > 0:
    if y2 < 0:
        status = False
else:
    if y2 > 0:
        status = False

if status:
    print('YES')
else:
    print('NO')
