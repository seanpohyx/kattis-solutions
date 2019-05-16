#https://open.kattis.com/problems/romans

roman_paces = 1000 * (5280/4854)
x = float(input())
print(round(x * roman_paces))
