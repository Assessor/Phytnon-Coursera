'''
На доске стоит белая шашка. Требуется определить, может ли она попасть в заданную клетку,
делая ходы по правилам (не превращаясь в дамку).
Белые шашки могут ходить по черным клеткам по диагонали вверх-влево
или вверх-вправо. Ходов может быть несколько!
'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x = ((x1 + y1) % 2 == 0) and ((x2 + y2) % 2 == 0)
y = (((x1 + y1) % 2 != 0) and ((x2 + y2) % 2 != 0))

if x or y:
    if y2 > y1:
        if (y2 - y1) >= (x2 - x1):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')
