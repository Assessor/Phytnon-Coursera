N = int(input())

hours = N // 60
minutes = N % 60
print(hours % 24, minutes)
