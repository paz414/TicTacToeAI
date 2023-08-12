bestMove=[0,0]
def display(Board):
    for i in range(0, 5):
        for j in range(0, 5):
            print(Board[i][j], end=(""))
        print()
def isFill(Board):
    for i in range(0,5,2):
        for j in range(0,5,2):
            if Board[i][j]=="   ":
                return False
    return True
def isEmpty(i,j):
    if(Board[i][j]=="   "):
        return True
    return False
def Wins(Board):
    for i in range(0, 5, 2):
        if Board[i][0] == Board[i][2] and Board[i][2] == Board[i][4]:
            if Board[i][0] == User:
                return -1
            if Board[i][0] == Comp:
                return 1
    for i in range(0, 5, 2):
        if Board[0][i] == Board[2][i] and Board[2][i] == Board[4][i]:
            if Board[0][i] == User:
                return -1
            if Board[0][i] == Comp:
                return 1
    if Board[0][0] == Board[2][2] and Board[2][2] == Board[4][4]:
        if Board[0][0] == User:
            return -1
        if Board[0][0] == Comp:
            return 1
    if Board[4][0] == Board[2][2] and Board[2][2] == Board[0][4]:
        if Board[4][0] == User:
            return -1
        if Board[4][0] == Comp:
            return 1
    return 0
def CompMove():
    bestScore=-100
    for i in range(0, 5, 2):
        for j in range(0, 5, 2):
            if isEmpty(i, j):
                Board[i][j]=Comp
                score=minimax(False)
                Board[i][j]="   "
                if score>bestScore:
                    bestScore =score
                    bestMove[0]=i
                    bestMove[1]=j
def minimax(isMax):
    result=Wins(Board)
    if result!=0:
        return result
    if isFill(Board) and result==0:
        return 0
    if isMax:
        bestScore=-100
        for i in range(0, 5, 2):
            for j in range(0, 5, 2):
                if isEmpty(i, j):
                    Board[i][j] = Comp
                    score = minimax(False)
                    Board[i][j] = "   "
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = 100
        for i in range(0, 5, 2):
            for j in range(0, 5, 2):
                if isEmpty(i, j):
                    Board[i][j] = User
                    score = minimax(True)
                    Board[i][j] = "   "
                    if score < bestScore:
                        bestScore = score
        return bestScore
Board=[
    ["   ", " | ", "   ", " | ", "   "],
    [" _ ", "   ", " _ ", "   ", " _ "],
    ["   ", " | ", "   ", " | ", "   "],
    [" _ ", "   ", " _ ", "   ", " _ "],
    ["   ", " | ", "   ", " | ", "   "]
]
display(Board)
d = int(input("Choose O or X by pressing 1 or 2 respectively : "))
Choice = ["O", "X"]
User = " " + Choice[d - 1] + " "
Comp = " " + Choice[2 - d] + " "
CompWin = False
UserWin = False
while True:

    while True:
        CoordIn = [int(input(f"Enter X-Coordinate for{User}: ")), int(input(f"Enter Y-Coordinate for{User}: "))]
        if isEmpty(2 * (CoordIn[0] - 1), 2 * (CoordIn[1] - 1)):
            Board[2 * (CoordIn[0] - 1)][2 * (CoordIn[1] - 1)] = User
            break
        else:
            print("Cell already Occupied! Try again.")
    display(Board)
    print("\n")
    if Wins(Board) == -1:
        UserWin = True
        break
    if Wins(Board) == 1:
        CompWin = True
        break
    if isFill(Board):
        break
    CompMove()
    CoordComp = [bestMove[0], bestMove[1]]
    Board[CoordComp[0]][CoordComp[1]] = Comp
    display(Board)
    print("\n")
    print("---------------------")
    if Wins(Board) == -1:
        UserWin = True
        break
    if Wins(Board) == 1:
        CompWin = True
        break
    if isFill(Board):
        break
if CompWin:
    print(f"{Comp}Wins")
elif UserWin:
    print(f"{User}Wins")
else:
    print("Draw !")