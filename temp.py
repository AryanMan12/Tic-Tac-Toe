from audioop import minmax


board = [[" ", "|", " ", "|", " "],
         ["-", "+", "-", "+", "-"],
         [" ", "|", " ", "|", " "],
         ["-", "+", "-", "+", "-"],
         [" ", "|", " ", "|", " "]]

marker = {
    '1': [0, 0],
    '2': [0, 2],
    '3': [0, 4],
    '4': [2, 0],
    '5': [2, 2],
    '6': [2, 4],
    '7': [4, 0],
    '8': [4, 2],
    '9': [4, 4],
}

live_vals = {
    '1': ' ',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': ' ',
    '6': ' ',
    '7': ' ',
    '8': ' ',
    '9': ' ',
}
# hello


def check_win(live_val):
    l_vals = list(live_val.values())
    # row col
    for i in range(3):
        if (l_vals[i*3] == l_vals[(i*3)+1] == l_vals[(i*3)+2]) and (l_vals[i*3] != " "):
            return l_vals[i*3]
        if (l_vals[i] == l_vals[i+3] == l_vals[i+6]) and (l_vals[i] != " "):
            return l_vals[i]
    # diagonals
    if (l_vals[0] == l_vals[4] == l_vals[8]) and (l_vals[4] != " "):
        return l_vals[4]

    elif (l_vals[2] == l_vals[4] == l_vals[6]) and (l_vals[4] != " "):
        return l_vals[4]
    # draw
    for i in range(len(l_vals)):
        if l_vals[i] == ' ':
            break
    else:
        return "tie"
    return " "


def minimax(vals):
    depth = list(vals.values()).count(" ")

    bestmove = ''
    for i in list(vals.keys()):
        if vals[i] == " ":
            vals[i] = "o"
            maximizer(vals, depth)


def minimizer(vals, depth):
    res = check_win(vals)
    if res != " ":
        return evaluate(vals, depth)


def maximizer(vals, depth):
    pass


def evaluate(vals, depth):
    res = check_win(vals)
    if res == "x":
        return -1*depth
    elif res == "o":
        return depth
    else:
        return 0


for x in board:
    for y in x:
        print(y, end="")
    print()


turn = True

while True:

    if turn and sel_box == " ":
        mark = input("Enter a box number: ")
        sel_box = board[marker.get(mark)[0]][marker.get(mark)[1]]
        sel_box = "x"
        live_vals[mark] = "x"
        turn = False
    elif not turn:
        mark = minimax(live_vals.copy())
        sel_box = board[marker.get(mark)[0]][marker.get(mark)[1]]
        sel_box = "o"
        live_vals[mark] = "o"
        turn = True
    else:
        print("Already taken!")

    board[marker.get(mark)[0]][marker.get(mark)[1]] = sel_box

    for x in board:
        for y in x:
            print(y, end="")
        print()

    res = check_win(live_vals)
    if res != " ":
        if (res == "tie"):
            print("Draw")
        else:
            print(f"{res} is the Winner")
        break

    if mark == "exit":
        break
