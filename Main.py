from tkinter import *
root = Tk()
root.geometry("325x550")
root.title("Tic Tac Toe")

root.resizable(0,0)

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 26), bg="lightpink", width=17)
titleLabel.grid(row=0, column=0)

optionalFrame = Frame(root, bg="grey")
optionalFrame.pack()

frame2 = Frame(root, bg="black")
frame2.pack()

board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

turn = "X"
game_end = False
mode="singlePlayer"

def changeToSinglePlayerMode():
    global mode
    mode = "singlePlayer"
    AIbutton["bg"]="lightgrey"
    Multibutton["bg"]="violet"

def changeToMultiPlayerMode():
    global mode
    mode = "multiPlayer"
    Multibutton["bg"]="lightgrey"
    AIbutton["bg"]="violet"

def updateBoard():
    for key in board.keys():
        buttons[key-1]["text"] = board[key]

def checkForWin(player):
    #all rows
    if board[1]==board[2]==board[3] and board[3]==player:
        return True
    elif board[4]==board[5]==board[6] and board[6]==player:
        return True
    if board[7]==board[8]==board[9] and board[9]==player:
        return True
    
    #all cols
    if board[1]==board[4]==board[7] and board[7]==player:
        return True
    if board[2]==board[5]==board[8] and board[8]==player:
        return True
    if board[3]==board[6]==board[9] and board[9]==player:
        return True
    
    #all diagonals
    if board[1]==board[5]==board[9] and board[9]==player:
        return True
    elif board[3]==board[5]==board[7] and board[7]==player:
        return True
    return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def minimax(board, isMiximizing):
    if checkForWin("O"):
        return 1
    if checkForWin("X"):
        return -1
    if checkForDraw():
        return 0
    if isMiximizing:
        bestScore = -100
        
        for key in board.keys():
            if board[key]==" ":
                board[key] = "O"
                score = minimax(board, False)
                board[key] = " "
                if score > bestScore:
                    bestScore = score
                    
        return bestScore
    else:
        bestScore = 100
        
        for key in board.keys():
            if board[key]==" ":
                board[key] = "X"
                score = minimax(board, True)
                board[key] = " "
                if score < bestScore:
                    bestScore = score

        return bestScore
                    
def AIplays():
    bestScore = -100
    bestMove = 0
    for key in board.keys():
        if board[key]==" ":
            board[key] = "O"
            score = minimax(board, False)
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key
    board[bestMove]="O"

def play(event):
    global turn
    global game_end

    if game_end:
        return
    
    button = event.widget
    buttonNO = str(button)
    clicked = buttonNO[-1]
    if clicked=="n":
        clicked=1
    else:
        clicked=int(clicked)


    if button["text"]==" ": 
        if turn=="X":
            board[clicked] = turn
            if checkForWin(turn): 
                WinningLabel = Label(frame1, text=f"{turn} wins the game", bg="orange", font=("Arial", 26), width=17)
                WinningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "O"
            updateBoard()

            if mode=="singlePlayer":
                AIplays()

                if checkForWin(turn): 
                    WinningLabel = Label(frame1, text=f"{turn} wins the game", bg="orange", font=("Arial", 26), width=17)
                    WinningLabel.grid(row=0, column=0, columnspan=3)
                    game_end = True

                turn="X"
                updateBoard()

        else:
            board[clicked]= turn
            updateBoard()
            if checkForWin(turn): 
                WinningLabel = Label(frame1, text=f"{turn} wins the game", bg="orange", font=("Arial", 26), width=17)
                WinningLabel.grid(row=0, column=0, columnspan=3)
                game_end = True
            turn = "X"


        if checkForDraw():
            DrawLabel = Label(frame1, text="Game draw", bg="orange", font=("Arial", 26), width=17)
            DrawLabel.grid(row=0, column=0, columnspan=3)

        

def restartGame():
    global game_end
    game_end=False
    for button in buttons:
        button["text"] = " "

    for i in board.keys():
        board[i] = " "

    titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30), bg="lightpink", width=15)
    titleLabel.grid(row=0, column=0)

#---------------UI--------------------------
#tic tac toe board

#change mode options
AIbutton = Button(optionalFrame, text="Single Mode", width=14, height=1, font=("Arial", 15), bg="violet", relief=RAISED, border=5, command=changeToSinglePlayerMode)
AIbutton.grid(row=0, column=0, columnspan=1, sticky=NW)

Multibutton = Button(optionalFrame, text="Multiple Mode", width=14, height=1, font=("Arial", 15), bg="violet", relief=RAISED, border=5, command=changeToMultiPlayerMode)
Multibutton.grid(row=0, column=1, columnspan=1, sticky=NW)


#first row

button1 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button1.grid(row=0, column=0)
button1.bind("<Button-1>", play)

button2 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button2.grid(row=0, column=1)
button2.bind("<Button-1>", play)

button3 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button3.grid(row=0, column=2)
button3.bind("<Button-1>", play)

#second row

button4 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", play)

button5 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", play)

button6 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", play)

#third row

button7 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button7.grid(row=2, column=0)
button7.bind("<Button-1>", play)

button8 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button8.grid(row=2, column=1)
button8.bind("<Button-1>", play)

button9 = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), bg="lightblue", relief=RAISED, borderwidth=5)
button9.grid(row=2, column=2)
button9.bind("<Button-1>", play)


restartButton = Button(frame2, text="Restart Game", width=20, height=1, font=("Arial", 19), bg="lightgreen", relief=RAISED, border=5, command=restartGame)
restartButton.grid(row=4, column=0, columnspan=5)

buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]


root.mainloop()