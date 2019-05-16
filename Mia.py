#https://open.kattis.com/problems/mia

def checkPairs(lst):
   return lst[1:] == lst[:-1]

while(True):
    die = [int(x) for x in input().split()]

    if sum(die) == 0:
        break
    #pairs = 2;4;6;8;10;12
    #winning = 3;
    player1 = [die[0], die[1]]
    player2 = [die[2], die[3]]
    player1.sort(reverse=True)
    player2.sort(reverse=True)

    if sum(player1) == 3 and sum(player2) != 3:
        print("Player 1 wins.")
    elif sum(player1) != 3 and sum(player2) == 3:
        print("Player 2 wins.")
    elif sum(player1) == 3 and sum(player2) == 3:
        print("Tie.")
    elif checkPairs(player1) == True and checkPairs(player2) != True:
        print("Player 1 wins.")
    elif checkPairs(player1)  != True and checkPairs(player2) == True:
        print("Player 2 wins.")
    elif checkPairs(player1) == True and checkPairs(player2) == True:
        #both are pairs
        if player1[0] > player2[0]:
            print("Player 1 wins.")
        elif player1[0] < player2[0]:
            print("Player 2 wins.")
        else:
            print("Tie.")
    else:
        valueOfP1 = int(''.join(str(x) for x in player1))
        valueOfP2 = int(''.join(str(x) for x in player2))

        if valueOfP1 > valueOfP2:
            print("Player 1 wins.")
        elif valueOfP1 < valueOfP2:
            print("Player 2 wins.")
        else:
            print("Tie.")