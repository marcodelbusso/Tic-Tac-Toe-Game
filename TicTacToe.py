from tkinter import *
from tkinter import messagebox
from time import sleep

bclick = [True] #Value used to change between 'X' and 'O'. X is true, O is false.

master = Tk()
master.resizable(0,0) #Makes the window non-resizable
frame = Frame(master, width=3, height=576, bg="", colormap="new")
frame.pack()
master.title("Tic Tac Toe") #Sets the title for the window

xCurrentScore = StringVar() #Label has to be updated with a textvariable, so score must be a string variable
oCurrentScore = StringVar() #Label has to be updated with a textvariable, so score must be a string variable

xCurrentScoreList = [0] #Stores X score value in an array so it can be updated from within a function
oCurrentScoreList = [0] #Stores O score value in an array so it can be updated from within a function

LabelX = Label(textvariable = xCurrentScore,font = ('Arial 30')) #Displays the current score for X in the GUI
LabelX.pack(side = LEFT, padx = 10) #Formatting

LabelO = Label(textvariable = oCurrentScore,font = ('Arial 30')) #Displays the current score for O in the GUI
LabelO.pack(side = RIGHT, padx = 20) #Formatting

xCurrentScore.set("X's Score:   " + str(xCurrentScoreList[0])) #Tells LabelX what to display in the GUI 
oCurrentScore.set("O's Score:   " + str(oCurrentScoreList[0])) #Tells LabelO what to display in the GUI

buttonsList = [" "," "," "," "," "," "," "," "," "] #Holds the

def computerOrAI():
    modeSelection = Toplevel()
    modeSelection.title("Choose Game Type")
    modeSelection.minsize(320,120)
    modeSelection.maxsize(320,120)
    modeSelection.resizable(0,0)
    modeSelection.geometry('320x120+800+400')
    modeSelection.attributes("-topmost", True)
 
    msg = Label(modeSelection, text="Would you like to play against the computer", font = ('Arial 12'))
    msg.pack(pady = 5)

    msg1 = Label(modeSelection, text="or another player?", font = ('Arial 12'))
    msg1.pack()

    buttonAI = Button(modeSelection, text="Against the AI", font = ('Arial 15 bold'), command = lambda: buttonAIDestruction())
    buttonAI.pack(side = LEFT, padx = 5)

    buttonPlayer = Button(modeSelection, text="Another Player", font = ('Arial 15 bold'), command = lambda: buttonAIDestruction())
    buttonPlayer.pack(side = RIGHT, padx = 5)

    def buttonAIDestruction():
        modeSelection.destroy()
        playerSelection()

def playerSelection():
    playerSelect = Toplevel()
    playerSelect.title("X/O")
    playerSelect.minsize(250,100)
    playerSelect.maxsize(250,100)
    playerSelect.resizable(0,0)
    playerSelect.geometry('250x100+800+400')
    playerSelect.attributes("-topmost", True)

    msg = Label(playerSelect, text="Which player will start first?",  font = ('Arial 12'))
    msg.pack(pady = 10)

    buttonX = Button(playerSelect, text="Player 'X'", font = ('Arial 15 bold'), command = lambda: xButtonClick())
    buttonX.pack(side = LEFT, padx = 5)

    buttonO = Button(playerSelect, text="Player 'O'", font = ('Arial 15 bold'), command = lambda: oButtonClick())
    buttonO.pack(side = RIGHT, padx = 5)

    def xButtonClick():
        bclick[0] = True
        playerSelect.destroy()

    def oButtonClick():
        bclick[0] = False
        playerSelect.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()

def tictactoe(button, listValue): 
    global bclick
    if buttonsList[listValue] == " " and bclick[0] == True:
        button["text"] = "X"
        buttonsList[listValue] = "X"
        bclick[0] = False
        scoreChecker()
        print(buttonsList) #Debug
        print(bclick) #Debug
        
    elif buttonsList[listValue] == " " and bclick[0] == False: #Checks if the button has a value in it or not
        button["text"] = "O"
        buttonsList[listValue] = "O"
        bclick[0] = True
        scoreChecker()
        print(buttonsList) #Debug
        print(bclick) #Debug

def scoreChecker(): #Checks all possible combinations for a win
    if(buttonsList[0] == "X" and buttonsList[1] == "X" and buttonsList[2] == "X" or
         buttonsList[0] == "X" and buttonsList[4] == "X" and buttonsList[8] == "X" or
         buttonsList[0] == "X" and buttonsList[3] == "X" and buttonsList[6] == "X" or
         buttonsList[3] == "X" and buttonsList[4] == "X" and buttonsList[5] == "X" or
         buttonsList[6] == "X" and buttonsList[7] == "X" and buttonsList[8] == "X" or
         buttonsList[2] == "X" and buttonsList[4] == "X" and buttonsList[6] == "X" or
         buttonsList[1] == "X" and buttonsList[4] == "X" and buttonsList[7] == "X" or
         buttonsList[2] == "X" and buttonsList[5] == "X" and buttonsList[8] == "X" ):
         messagebox.showinfo("THE WINNER IS X","PLAYER X WON THE GAME")
         xCurrentScoreList[0] = xCurrentScoreList[0] + 1
         clearBoard()
         xCurrentScore.set("X's Score:   " + str(xCurrentScoreList[0]))
         computerOrAI()
         
    elif(buttonsList[0] == "O" and buttonsList[1] == "O" and buttonsList[2] == "O" or
        buttonsList[0] == "O" and buttonsList[4] == "O" and buttonsList[8] == "O" or
        buttonsList[0] == "O" and buttonsList[3] == "O" and buttonsList[6] == "O" or
        buttonsList[3] == "O" and buttonsList[4] == "O" and buttonsList[5] == "O" or
        buttonsList[6] == "O" and buttonsList[7] == "O" and buttonsList[8] == "O" or
        buttonsList[2] == "O" and buttonsList[4] == "O" and buttonsList[6] == "O" or
        buttonsList[1] == "O" and buttonsList[4] == "O" and buttonsList[7] == "O" or
        buttonsList[2] == "O" and buttonsList[5] == "O" and buttonsList[8] == "O" ):
        messagebox.showinfo("THE WINNER IS O","PLAYER O WON THE GAME")
        oCurrentScoreList[0] = oCurrentScoreList[0] + 1
        clearBoard()
        oCurrentScore.set("O's Score:   " + str(oCurrentScoreList[0]))
        computerOrAI()
         
    elif((buttonsList[0] == "O" or buttonsList[0] == "X") and (buttonsList[1] == "O" or
         buttonsList[1] == "X") and (buttonsList[2] == "O" or buttonsList[2] == "X") and
         (buttonsList[3] == "O" or buttonsList[3] == "X") and (buttonsList[4] == "O" or
         buttonsList[4] == "X") and (buttonsList[5] == "O" or buttonsList[5] == "X") and
         (buttonsList[6] == "O" or buttonsList[6] == "X") and (buttonsList[7] == "O" or
         buttonsList[7] == "X") and (buttonsList[8] == "O" or buttonsList[8] == "X") ):
         messagebox.showinfo("NOBODY WINS","THE GAME IS A TIE")
         clearBoard()
         computerOrAI()

def clearBoard(): #Resets the board to a default state in the list and the actual button text
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

#Defining each button to be generated with tkinter

button1 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button1,0))
button1.grid(row = 1, column = 0)

button2 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button2,1))
button2.grid(row = 1, column = 1)

button3 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button3,2))
button3.grid(row = 1, column = 2)

button4 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button4,3))
button4.grid(row = 2, column = 0)

button5 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button5,4))
button5.grid(row = 2, column = 1)

button6 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button6,5))
button6.grid(row = 2, column = 2)

button7 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button7,6))
button7.grid(row = 3, column = 0)

button8 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button8,7))
button8.grid(row = 3, column = 1)

button9 = Button(frame, text = " ", font = ('Arial 30 bold'), height = 4, width = 8, command = lambda: tictactoe(button9,8))
button9.grid(row = 3, column = 2)

master.geometry('605x710+660+180')

computerOrAI()

master.protocol("WM_DELETE_WINDOW", on_closing) #Generates an event for when the user presses the close button on the window
master.iconbitmap('elicon.ico') #Changes the default window icon
mainloop()
