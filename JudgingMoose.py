#https://open.kattis.com/problems/judgingmoose

noOfTines = [int(n) for n in input().split()]
highest = 0

if noOfTines[0] > noOfTines[1]:
    highest = noOfTines[0]
else:
    highest = noOfTines[1]


if noOfTines[0] == 0 and noOfTines[1] == 0:
    print("Not a moose")
elif noOfTines[0] != noOfTines[1]:
    print("Odd " + str(highest*2))
else:
    print("Even " + str(highest*2))


