h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = s1 + (m1 * 60) + (h1 * 3600)
t2 = s2 + (m2 * 60) + (h2 * 3600)

print(t2 - t1)
