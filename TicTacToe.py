from tkinter import *
from tkinter import messagebox
from time import sleep
from random import randint

##import davidclient
##c = davidclient.Client()
##
##try:
##    while True:
##        messages = c.poll()
##except davidclient.NotConnected:
##    pass

    


bclick = [True] #Value used to change between 'X' and 'O'. X is true, O is false.
AISelectionBool = [False] #Value used to determine if player wishes to play against the AI in a later function

master = Tk() #The main board frame
master.withdraw() #Hides the main board so only the game type selection window is shown
master.resizable(0,0) #Makes the window non-resizable
master.attributes("-topmost", True)
frame = Frame(master, width=3, height=576, bg="", colormap="new") #Formatting
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

buttonsList = [" "," "," "," "," "," "," "," "," "] #Holds the value for each button to be used for game win check comparisons

#Defining each button to be generated with tkinter

button1 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button1,0))
button1.grid(row = 1, column = 0)

button2 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button2,1))
button2.grid(row = 1, column = 1)

button3 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button3,2))
button3.grid(row = 1, column = 2)

button4 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button4,3))
button4.grid(row = 2, column = 0)

button5 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button5,4))
button5.grid(row = 2, column = 1)

button6 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button6,5))
button6.grid(row = 2, column = 2)

button7 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button7,6))
button7.grid(row = 3, column = 0)

button8 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button8,7))
button8.grid(row = 3, column = 1)

button9 = Button(frame, font = ('Arial 30 bold'), text = " ", height = 3, width = 6, command = lambda: tictactoe(button9,8))
button9.grid(row = 3, column = 2)

master.geometry('605x710+660+180')

def computerOrAI():
    modeSelection = Toplevel()
    modeSelection.title("Choose Game Type")
    modeSelection.minsize(320,120) #Makes the window un-resizable
    modeSelection.maxsize(320,120)
    modeSelection.resizable(0,0) #Disables the 'Maximise' button
    modeSelection.geometry('320x120+800+400')
    modeSelection.attributes("-topmost", True) #Keeps the window on the top
 
    msg = Label(modeSelection, text="Would you like to play against the computer", font = ('Arial 12'))
    msg.pack(pady = 5)

    msg1 = Label(modeSelection, text="or another player?", font = ('Arial 12'))
    msg1.pack()

    buttonAI = Button(modeSelection, text="Against the AI", font = ('Arial 15 bold'), command = lambda: randomAI())
    buttonAI.pack(side = LEFT, padx = 5)

    buttonPlayer = Button(modeSelection, text="Another Player", font = ('Arial 15 bold'), command = lambda: buttonAIDestruction())
    buttonPlayer.pack(side = RIGHT, padx = 5)

    def buttonAIDestruction():
        modeSelection.destroy()
        playerSelection()

    def randomAI():
        AISelectionBool[0] = True
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
        clearBoard()
        serverConnectionWindowSettings()

    def oButtonClick():
        bclick[0] = False
        playerSelect.destroy()
        clearBoard()
        serverConnectionWindowSettings()

def serverConnectionWindowSettings():
    serverOptions = Toplevel()
    serverOptions.title("Server Op's")
    serverOptions.minsize(200,80)
    serverOptions.maxsize(200,80)
    serverOptions.resizable(0,0)
    serverOptions.geometry('200x80+800+400')
    serverOptions.attributes("-topmost", True)

    hostNameLabel = Label(serverOptions, text="Host Name", font = ('Arial 10 bold')).grid(row=0)
    portLabel = Label(serverOptions, text="Port          ", font = ('Arial 10 bold')).grid(row=1)

    hostNameTxtBox = Entry(serverOptions)
    portTxtBox = Entry(serverOptions)

    hostNameTxtBox.grid(row = 0, column = 1)
    portTxtBox.grid(row = 1, column = 1)

    buttonSubmit = Button(serverOptions, text="Submit", font = ('Arial 10 bold'), command = lambda: buttonClick()).grid(row = 3, column = 0)

    def buttonClick():
        #Server settings connection code
        master.update()
        master.deiconify()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        master.destroy()

def tictactoe(button, listValue):

    global bclick

    def AIRunCheck():

        def buttonCheckAssignment(letter, number):
            if number == 0:
                button1["text"] = letter
                buttonsList[0] = letter
            elif number == 1:
                button2["text"] = letter
                buttonsList[1] = letter
            elif number == 2:
                button3["text"] = letter
                buttonsList[2] = letter
            elif number == 3:
                button4["text"] = letter
                buttonsList[3] = letter
            elif number == 4:
                button5["text"] = letter
                buttonsList[4] = letter
            elif number == 5:
                button6["text"] = letter
                buttonsList[5] = letter
            elif number == 6:
                button7["text"] = letter
                buttonsList[6] = letter
            elif number == 7:
                button8["text"] = letter
                buttonsList[7] = letter
            elif number == 8:
                button9["text"] = letter
                buttonsList[8] = letter

        def buttonNumAssignment(buttonValU):
            if bclick[0] == True:
                buttonCheckAssignment("X", buttonValU)
                bclick[0] = False
            else:
                buttonCheckAssignment("O", buttonValU)
                bclick[0] = True
            
        if scoreChecker() == None:            
            if AISelectionBool[0] == True:
                randNum = randint(0,8)
                randomButton = buttonsList[randNum]              
                if randomButton != " ":
                    AIRunCheck()
                else:
                    buttonNumAssignment(randNum)
                        
    if buttonsList[listValue] == " " and bclick[0] == True:
        button["text"] = "X"
        buttonsList[listValue] = "X"
        bclick[0] = False
        AIRunCheck()
        scoreChecker()
        print(buttonsList) #Debug
        print(bclick) #Debug
        
    elif buttonsList[listValue] == " " and bclick[0] == False: #Checks if the button has a value in it or not
        button["text"] = "O"
        buttonsList[listValue] = "O"
        bclick[0] = True
        AIRunCheck()
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
         master.withdraw()
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
        master.withdraw()
        computerOrAI()
         
    elif((buttonsList[0] == "O" or buttonsList[0] == "X") and (buttonsList[1] == "O" or
         buttonsList[1] == "X") and (buttonsList[2] == "O" or buttonsList[2] == "X") and
         (buttonsList[3] == "O" or buttonsList[3] == "X") and (buttonsList[4] == "O" or
         buttonsList[4] == "X") and (buttonsList[5] == "O" or buttonsList[5] == "X") and
         (buttonsList[6] == "O" or buttonsList[6] == "X") and (buttonsList[7] == "O" or
         buttonsList[7] == "X") and (buttonsList[8] == "O" or buttonsList[8] == "X") ):
         messagebox.showinfo("NOBODY WINS","THE GAME IS A TIE")
         clearBoard()
         master.withdraw()
         computerOrAI()

    else:
        return None

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

computerOrAI()

master.protocol("WM_DELETE_WINDOW", on_closing) #Generates an event for when the user presses the close button on the window
master.iconbitmap('elicon.ico') #Changes the default window icon
mainloop()
