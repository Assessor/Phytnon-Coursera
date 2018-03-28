'''
Для данного числа n<100 закончите фразу “На лугу пасется...”
одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.
'''
n = int(input())

tmp = n
if n > 20:
    n = n % 10

if n == 0 or (5 <= n <= 20):
    print(tmp, 'korov')
elif n == 1:
    print(tmp, 'korova')
elif n == 2 or n == 3 or n == 4:
    print(tmp, 'korovy')
