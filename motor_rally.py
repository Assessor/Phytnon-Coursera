'''
За день машина проезжает N километров. Сколько дней нужно, чтобы проехать маршут длиной M километров?
'''
N = int(input())
M = int(input())

print((N + M - 1) // N)