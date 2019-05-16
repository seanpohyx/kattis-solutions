#https://open.kattis.com/problems/2048

rows = [0] * 4;
for i in range(4):
    rows[i] = [int(n) for n in input().split()]

direction = int(input())

def swipeLeft(rows):
    for i in range(4):
        j = 0
        while j < 4:
            if rows[i][j] != 0:
                for k in range(j+1,4):
                    if rows[i][k] == 0:
                        continue
                    elif rows[i][j] == rows[i][k]:
                        rows[i][j] += rows[i][k]
                        rows[i][k] = 0
                        break
                    else:
                        break
            else:
                for k in range(j+1,4):
                    if rows[i][k] == 0:
                        continue
                    elif rows[i][k] != 0:
                        rows[i][j] = rows[i][k]
                        rows[i][k] = 0
                        j-=1
                        break
                    else:
                        break
            j+=1


    return rows

def rotate(direction, rows):
    # input integer 0, 1, 2, or 3 that denotes a left, up, right, or down move
    temp = [row[:] for row in rows]
    if direction == "left":
        #rotate left
        for i in range(4):
            for j in range(4):
                temp[i][j] = rows[j][3-i]
    elif direction == "inverse":
        #rotate 180
        for i in range(4):
            for j in range(4):
                temp[i][j] = rows[i][3-j]
    elif direction == "right":
        #rotate right
        for i in range(4):
            for j in range(4):
                temp[i][j] = rows[3-j][i]

    return temp


def swipe(direction, rows):
    temp = rows
    if direction == 0:
        #swipe left
        temp = swipeLeft(temp)
    elif direction == 1:
        #swipe up
        temp = rotate("left", temp) #rotate left
        temp = swipeLeft(temp)
        temp = rotate("right", temp)
    elif direction == 2:
        #swipe right
        temp = rotate("inverse", temp)  # rotate 180
        temp = swipeLeft(temp)
        temp = rotate("inverse", temp)  # rotate 180
    elif direction == 3:
        #swipe down
        temp = rotate("right", temp)  # rotate 180
        temp = swipeLeft(temp)
        temp = rotate("left", temp)  # rotate 180

    for row in temp:
        printedRow = ""
        for value in row:
            printedRow += (str(value) + " ")
        print(printedRow)


swipe(direction, rows)


