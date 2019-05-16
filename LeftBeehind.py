#https://open.kattis.com/problems/leftbeehind


while (True):
    beecision = [int(x) for x in input().split()]
    if sum(beecision) == 0:
        break
    if sum(beecision) == 13:
        print("Never speak again.")
    elif beecision[0] > beecision[1]:
        print("To the convention.")
    elif beecision[0] < beecision[1]:
        print("Left beehind.")
    elif beecision[0] == beecision[1]:
        print("Undecided.")