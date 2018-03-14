A = int(input())
B = int(input())

x = (1 // (A % B + 1) + 1) % 2
y = 1 // (A % B + 1)

print('NO' * x + 'YES' * y)
