from tkinter import *
from tkinter import messagebox

master = Tk()
master.resizable(0,0)
frame = Frame(master, width=3, height=576, bg="", colormap="new")
frame.pack()
master.title("Tic Tac Toe")

xCurrentScore = StringVar()
oCurrentScore = StringVar()

xCurrentScoreList = [0]
oCurrentScoreList = [0]

LabelX = Label(textvariable = xCurrentScore,font = ('Arial 30'))
LabelX.pack(side = LEFT, padx = 10)

LabelO = Label(textvariable = oCurrentScore,font = ('Arial 30'))
LabelO.pack(side = RIGHT, padx = 20)

## HAVE TO FIGURE OUT HOW TO UPDATE A LABEL WHILE CALLING FROM WITHIN SCORECHECKER

xCurrentScore.set("X's Score:   " + str(xCurrentScoreList[0]))
oCurrentScore.set("O's Score:   " + str(oCurrentScoreList[0]))

bclick = [True]

buttonsList = [" "," "," "," "," "," "," "," "," "]

def tictactoe(button, listValue):
    global bclick
    if buttonsList[listValue] == " " and bclick[0] == True:
        button["text"] = "X"
        buttonsList[listValue] = "X"
        bclick[0] = False
        scoreChecker()
        print(buttonsList)
        print(bclick)
        
    elif buttonsList[listValue] == " " and bclick[0] == False:
        button["text"] = "O"
        buttonsList[listValue] = "O"
        bclick[0] = True
        scoreChecker()
        print(buttonsList)
        print(bclick)

def scoreChecker():
    if(buttonsList[0] == "X" and buttonsList[1] == "X" and buttonsList[2] == "X" or
         buttonsList[0] == "X" and buttonsList[4] == "X" and buttonsList[8] == "X" or
         buttonsList[0] == "X" and buttonsList[3] == "X" and buttonsList[6] == "X" or
         buttonsList[3] == "X" and buttonsList[4] == "X" and buttonsList[5] == "X" or
         buttonsList[6] == "X" and buttonsList[7] == "X" and buttonsList[8] == "X" or
         buttonsList[2] == "X" and buttonsList[4] == "X" and buttonsList[6] == "X" or
         buttonsList[1] == "X" and buttonsList[4] == "X" and buttonsList[7] == "X" or
         buttonsList[2] == "X" and buttonsList[5] == "X" and buttonsList[8] == "X" ):
         bclick[0] = True
         messagebox.showinfo("THE WINNER IS X","PLAYER X WON THE GAME")
         xCurrentScoreList[0] = xCurrentScoreList[0] + 1
         print(xCurrentScoreList)
         clearBoard()
         xCurrentScore.set("X's Score:   " + str(xCurrentScoreList[0]))
         print(xCurrentScore.get())
         
    elif(buttonsList[0] == "O" and buttonsList[1] == "O" and buttonsList[2] == "O" or
        buttonsList[0] == "O" and buttonsList[4] == "O" and buttonsList[8] == "O" or
        buttonsList[0] == "O" and buttonsList[3] == "O" and buttonsList[6] == "O" or
        buttonsList[3] == "O" and buttonsList[4] == "O" and buttonsList[5] == "O" or
        buttonsList[6] == "O" and buttonsList[7] == "O" and buttonsList[8] == "O" or
        buttonsList[2] == "O" and buttonsList[4] == "O" and buttonsList[6] == "O" or
        buttonsList[1] == "O" and buttonsList[4] == "O" and buttonsList[7] == "O" or
        buttonsList[2] == "O" and buttonsList[5] == "O" and buttonsList[8] == "O" ):
        bclick[0] = True
        messagebox.showinfo("THE WINNER IS O","PLAYER O WON THE GAME")
        oCurrentScoreList[0] = oCurrentScoreList[0] + 1
        clearBoard()
        oCurrentScore.set("O's Score:   " + str(oCurrentScoreList[0]))
        print(oCurrentScore.get())
         
    elif((buttonsList[0] == "O" or buttonsList[0] == "X") and (buttonsList[1] == "O" or
         buttonsList[1] == "X") and (buttonsList[2] == "O" or buttonsList[2] == "X") and
         (buttonsList[3] == "O" or buttonsList[3] == "X") and (buttonsList[4] == "O" or
         buttonsList[4] == "X") and (buttonsList[5] == "O" or buttonsList[5] == "X") and
         (buttonsList[6] == "O" or buttonsList[6] == "X") and (buttonsList[7] == "O" or
         buttonsList[7] == "X") and (buttonsList[8] == "O" or buttonsList[8] == "X") ):
         bclick[0] = True
         messagebox.showinfo("NOBODY WINS","THE GAME IS A TIE")
         clearBoard()

def clearBoard():
    buttonsList[0] = " "
    buttonsList[1] = " "
    buttonsList[2] = " "
    buttonsList[3] = " "
    buttonsList[4] = " "
    buttonsList[5] = " "
    buttonsList[6] = " "
    buttonsList[7] = " "
    buttonsList[8] = " "
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "


button = StringVar()



button1 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button1,0))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button2,1))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button3,2))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button4,3))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button5,4))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button6,5))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button7,6))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button8,7))
button8.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button9,8))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

mainloop()
