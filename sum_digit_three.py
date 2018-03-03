'''
Дано трехзначное число. Найдите сумму его цифр.
'''
digit = int(input())
oneDigit = digit // 100
twoDigit = digit // 10 % 10
threeDigit = digit % 10
print(oneDigit + twoDigit + threeDigit)
