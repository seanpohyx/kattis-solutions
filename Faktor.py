#https://open.kattis.com/problems/faktor
#hint simple formula (I-1)*A + 1

values = [int(n) for n in input().split()]
a = values[0]
i = values[1]
print((i-1)*a + 1)