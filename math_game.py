#Use runGame() to open the window and start the game. 

import tkinter
import random
import math

mainWindow = None

problemType = None

tempType = None

correctAnswer = None

totalProblems = 0

totalGuesses = 0 

tempGuesses = None

probSolved = 0

aveAttempt = 0

probList = []

#Implements a tinker-based GUI program for a simple math game. All problems have positive integer answers. 

def checkGuess():
    global correctAnswer 
    global totalProblems
    global totalGuesses 
    global tempGuesses
    global probSolved 
    global aveAttempt
    
    if tempGuesses == 0: 
        totalProblems = totalProblems + 1
    
    tempGuesses = tempGuesses + 1
    guessString = guessEntry.get()
    if guessString.isdigit() == False:
        guess = None
    else:
        guess = int(guessString) 
    if guess == correctAnswer: 
        labelResponse.configure(text = "Correct!")
        submitButton.configure(state = tkinter.DISABLED)
        guessEntry.configure(state = tkinter.DISABLED)
        probSolved = probSolved + 1
        totalGuesses = totalGuesses + tempGuesses
        aveAttempt = totalGuesses / probSolved
        labelAve.configure(text = "Average # of attempts per problem: {}".format(aveAttempt))        
    else: 
        labelResponse.configure(text = "Incorrect. Please try again.")
    
    labelAttempt.configure(text = "Attempts on current problem: {}".format(tempGuesses))
    labelScore.configure(text = "Score: {} out of {} problems solved".format(probSolved, totalProblems))
    guessEntry.delete(0, tkinter.END)

def generateProblem(): 
    global problemType
    global tempType
    global correctAnswer 
    global tempGuesses
    global probList
    
    tempGuesses = 0 
    
    repeat = True
    
    submitButton.configure(state = tkinter.NORMAL)
    guessEntry.configure(state = tkinter.NORMAL)
    guessEntry.delete(0, tkinter.END)
    labelResponse.configure(text = "You haven't made any guesses yet.")
    labelAttempt.configure(text = "Attempts on current problem: {}".format(tempGuesses))
    numOne = None
    numTwo = None
    tempType = None
    if problemType.get() == 5: 
        tempType = random.randint(1, 4)
        
    if problemType.get() == 1 or tempType == 1: 
        numOne = random.randint(0, 999)
        numTwo = random.randint(0, 999)
        tempCheck = ("{} + {}".format(numOne, numTwo))
        if tempCheck not in probList:
            repeat = False
            labelProblem.configure(text = "{} + {} =".format(numOne, numTwo))
            correctAnswer = numOne + numTwo
            probList.append(tempCheck)

    elif problemType.get() == 2 or tempType == 2: 
        numOne = random.randint(0, 999)
        numTwo = random.randint(0, 999)
        if numOne > numTwo: 
            tempCheck = ("{} - {}".format(numOne, numTwo))
            if tempCheck not in probList:
                repeat = False
                labelProblem.configure(text = "{} - {} =".format(numOne, numTwo))
                correctAnswer = numOne - numTwo
                probList.append(tempCheck)
        else: 
            tempCheck = ("{} - {}".format(numTwo, numOne))
            if tempCheck not in probList:
                repeat = False
                labelProblem.configure(text = "{} - {} =".format(numTwo, numOne))
                correctAnswer = numTwo - numOne
                probList.append(tempCheck)
            
                
    elif problemType.get() == 3 or tempType == 3: 
        numOne = random.randint(0, 99)
        numTwo = random.randint(0, 99) 
        tempCheck = ("{} x {}".format(numOne, numTwo))
        if tempCheck not in probList:
            repeat = False
            labelProblem.configure(text = "{} x {} =".format(numOne, numTwo))
            correctAnswer = (numOne * numTwo)
            probList.append(tempCheck)
            
    elif problemType.get() == 4 or tempType == 4: 
        numOne = random.randint(1, 999)
        factorList = findFactors(numOne)
        if len(factorList) == 0: 
            numTwo = 1
            tempCheck = ("{} / {}".format(numOne, numTwo))
            if tempCheck not in probList:
                repeat = False
                labelProblem.configure(text = "{} / {}".format(numOne, numTwo))
                correctAnswer = numOne / numTwo
                probList.append(tempCheck)
        else: 
            numTwo = random.choice(factorList) 
            tempCheck = ("{} / {}".format(numOne, numTwo))
            if tempCheck not in probList:
                repeat = False
                labelProblem.configure(text = "{} / {} =".format(numOne, numTwo))
                correctAnswer = numOne / numTwo
                probList.append(tempCheck)
        if repeat == True:
            generateProblem()

def findFactors(num): 
    listy = [] 
    for element in range(2, num): 
        if num % element == 0: 
            listy.append(element)
    return listy 

def quitGame():
    print("Game Summary:")
    print("Number of problems attempted: {}".format(totalProblems))
    print("Number of problems solved: {}".format(probSolved))
    print("Average # of attempts per problem: {}".format(aveAttempt))
    mainWindow.destroy()


def initializeWindow():
    global mainWindow
    global problemType
    global labelProblem
    global guessEntry
    global labelResponse
    global submitButton
    global labelAttempt 
    global labelScore
    global labelAve

    
    mainWindow = tkinter.Tk()
    mainWindow.title("Fun Math Game")
    topFrame = tkinter.Frame(mainWindow, pady = 5)
    topFrame.pack()
    
    problemType = tkinter.IntVar()
    problemType.set(5)
    
    radio1 = tkinter.Radiobutton(topFrame, text = "Addition", variable = problemType, value=1, indicator = 0, background = "light coral")
    radio1.pack(side = tkinter.LEFT, ipady = 5)
    radio2 = tkinter.Radiobutton(topFrame, text = "Subtraction", variable = problemType, value=2, indicator = 0, background = "light goldenrod" )
    radio2.pack(side = tkinter.LEFT, ipady = 5)
    radio3 = tkinter.Radiobutton(topFrame, text = "Multiplication", variable = problemType, value=3, indicator = 0, background = "pale green")
    radio3.pack(side = tkinter.LEFT, ipady = 5)
    radio4 = tkinter.Radiobutton(topFrame, text = "Division", variable = problemType, value=4, indicator = 0, background = "light blue")
    radio4.pack(side = tkinter.LEFT, ipady = 5)    
    radio5 = tkinter.Radiobutton(topFrame, text = "Random Type", variable = problemType, value=5, indicator = 0, background = "thistle")
    radio5.pack(side = tkinter.LEFT, ipady = 5)     
    
    
    
    midFrame = tkinter.Frame(mainWindow)
    midFrame.pack()
    labelProblem = tkinter.Label(midFrame, text = "? + ? = ")
    labelProblem.pack(side=tkinter.LEFT)
    guessEntry = tkinter.Entry(midFrame)
    guessEntry.pack(side=tkinter.LEFT)
    
    lowerFrame = tkinter.Frame(mainWindow)
    lowerFrame.pack() 
    labelResponse = tkinter.Label(lowerFrame, text = "You haven't made any guesses yet.", pady = 5) 
    labelResponse.pack() 
    
    statsFrame = tkinter.Frame(mainWindow, bg = "misty rose", padx = 30, pady = 10, highlightcolor = "light coral", bd = 5, relief = "groove")
    statsFrame.pack()
    labelAttempt = tkinter.Label(statsFrame, text = "Attempts on current problem: 0", bg = "misty rose")
    labelAttempt.pack()       
    labelScore = tkinter.Label(statsFrame, text = "Score: 0 out of 0 problems solved", bg = "misty rose")
    labelScore.pack()    
    labelAve = tkinter.Label(statsFrame, text = "Average # of attempts per problem: 0", bg = "misty rose")
    labelAve.pack()
    
    
    bottomFrame = tkinter.Frame(mainWindow)
    bottomFrame.pack(side = tkinter.TOP)
    submitButton = tkinter.Button(bottomFrame, text = "SUBMIT ANSWER", state = tkinter.DISABLED, command = checkGuess)
    submitButton.pack(side = tkinter.LEFT, ipady = 5)
    newButton = tkinter.Button(bottomFrame, text = "NEW PROBLEM", command = generateProblem) 
    newButton.pack(side = tkinter.LEFT, ipady = 5)
    quitButton = tkinter.Button(bottomFrame, text = "QUIT GAME", command = quitGame) 
    quitButton.pack(side = tkinter.LEFT, ipady = 5)
    

#Use this to start the game and open the window. 

def runGame():
    initializeWindow()
    mainWindow.mainloop()
    
    
    
    
    

