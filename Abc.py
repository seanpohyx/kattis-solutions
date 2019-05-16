#https://open.kattis.com/problems/abc

numbers = input()
arrangements = input()

numbers = numbers.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()

# A < B < C
Dict = dict({'A': numbers[0], 'B': numbers[1], 'C': numbers[2]})

for i in range(len(arrangements)):
    print(Dict.get(arrangements[i]), end =" ")




