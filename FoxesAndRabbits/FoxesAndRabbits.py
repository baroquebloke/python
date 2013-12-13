# HW 8 -- Foxes and Rabbits

from Tkinter import *
from time import *
from random import *
from math import *
import sys

class MyWindow(Frame):
    def __init__(self, master=None):
        self.bgcolor = "yellow"
        Frame.__init__(self, master)
        self.grid()
        top = self.winfo_toplevel()
        top.title("Foxes and Rabbits")
        self.createWidgets()
        self.lastx = 0
        self.lasty = 0
                        
    def createWidgets(self):
        MenuBar = Frame(self)
        MenuBar.grid(sticky=NW)

        QuitButton = Button(MenuBar, text="Quit", command = self.quit)
        QuitButton.grid(row = 0, column = 0)

# Here are the Pause, Run, and Populate Buttons
        RunButton = Button(MenuBar, text="Run", command = RunPauseCallback)
        RunButton.grid(row = 1, column = 0)

        PauseButton = Button(MenuBar, text="Pause", command = RunPauseCallback)
        PauseButton.grid(row = 1, column = 1)

        PopulateButton = Button(MenuBar, text="Populate", command = PopulateCallback)
        PopulateButton.grid(row = 0, column = 1)
##############
# Here's the scale sliders
        global InitialNumberRabbits
        InitialNumberRabbits = IntVar()
        InitialNumberRabbits.set(33)
        Rabbits = Scale(MenuBar, from_=1, to=200, orient=HORIZONTAL, 
            variable = InitialNumberRabbits, command=RabbitCallback)
        Rabbits.grid(row=0, column  = 3)

        global InitialNumberFoxes
        InitialNumberFoxes = IntVar()
        InitialNumberFoxes.set(3)
        Foxes = Scale(MenuBar, from_=1, to=20, orient=HORIZONTAL, 
            variable = InitialNumberFoxes, command=FoxCallback)
        Foxes.grid(row=0, column  = 2)
##############
# Macho Bunny Factor!!!
        global MachoBunnyFactor
        defaultMacho = IntVar()
        defaultMacho.set(9)
        MachoBunnyFactor = Scale(MenuBar, from_=1, to=9, orient=HORIZONTAL, 
            variable = defaultMacho)
        MachoBunnyFactor.grid(row=0, column  = 4)
##############

        global GenerationField
        GenerationField = Label(MenuBar, text="Generation: 0")
        GenerationField.grid(row = 1, column = 4)
        
        global FoxField
        FoxField = Label(MenuBar, text="Foxes: 0")
        FoxField.grid(row = 1, column = 2)
        
        global RabbitField
        RabbitField = Label(MenuBar, text="Rabbits: 0")
        RabbitField.grid(row = 1, column = 3)

        global canvas
        canvas = Canvas(self, width=500, height=500, background=self.bgcolor)
        canvas.grid(row=1)
        self.canvas = canvas
        canvas.focus_set()

# A specific location for the callback functions was not specified.
# Should I have used seperate callback functions for pause and run?  
def RunPauseCallback():
    global PAUSE
    if PAUSE == True:
        PAUSE = False
        AnimationLoop()
    elif PAUSE == False:
        PAUSE = True
    

def PopulateCallback():
    RandomlyPopulateGrid()
                
######################
# Here's the scale slider callback functions
def RabbitCallback(scaleValue):
    global InitialNumberRabbits
    n = int(scaleValue)
    InitialNumberRabbits = n

def FoxCallback(scaleValue):
    global InitialNumberFoxes
    n = int(scaleValue)
    InitialNumberFoxes = n


#####################

def reportGenerations(n):
    # This updates the label with the generation number
    GenerationField.configure(text="Generation: %d" %n)
    GenerationField.update()

def reportFoxes():
    # This updates the label with the fox count
    FoxField.configure(text="Foxes: %d" %Fox.count)
    FoxField.update()
    
def reportRabbits():
    # This updates the label with the rabbit count
    RabbitField.configure(text="Rabbits: %d" %Rabbit.count)
    RabbitField.update()
    

class GridSquare:
    #  This class represents one square on the grid, where
    #  a fox ("red"), a rabbit ("blue") or grass ("green") might
    #  be.
    def __init__(self, shape):
        self.color = "green"
        self.shape = shape

    

class Grid:
    # This class represents the board where there are foxes and rabbits
    def __init__(self, rows, cols, size):
        self.rows = rows;
        self.cols = cols;
        start_y = 10
        self.RowList = []
        self.ColorRowList = []
        for i in range(0, rows):
            Row = []
            start_x = 10
            for j in range(0, cols):
                shape = canvas.create_rectangle(start_x, start_y,
                                                    start_x + size, start_y + size,
                                                    fill = "green")
                Row.append(GridSquare(shape))
                start_x = start_x + size+1
            start_y = start_y + size+1
            self.RowList.append(Row)

    def getColor(self, row, col):
        # This returns the color of the given row and column of the grid.
        Row = self.RowList[row]
        return Row[col].color
 
    def isEmpty(self, row, col):
        # Returns true if the given row and column of the grid is empty
        if self.getColor(row, col) == "green":
            return True
        else:
            return False

    def isLive(self, row, col):
        # Returns true if the given row and column of the grid is not empty
        return not self.isEmpty(row, col)
    
    def isRabbit(self, row, col):
        # Returns true if the given row and column of the grid is a rabbit
        if self.getColor(row, col) == "blue":
            return True
        else:
            return False
        
    def setColor(self, row, col, color):
        # Sets the color of the given row and column of the grid.
        # This does not change the AnimalList or NewAnimalList
        Row = self.RowList[row]
        entry = Row[col]
        entry.color = color
        canvas.itemconfigure(entry.shape, fill=color)
        canvas.update()
        
    def add(self, animal):
        # This adds an animal to the grid by looking up its info and
        # calling setColor()
        r = animal.row
        c = animal.col
        color = animal.color
        self.setColor(r, c, color)


class Animal:
    # This represents all animals: foxes and rabbits.
    # Note that there is no constructor -- you can't make
    # an  Animal that is neither a Fox nor a Rabbit.
        
    def oneYear(self):
        # This represents one iteration of the animal's life cycle:
        # grow older, eat, and reproduce.
        # This is the same for both foxes and rabbits.
        self.age = self.age + 1
        if self.age > self.maxAge:
            self.die()
        else:
            self.energy = self.energy - self.oneYearEnergy
            if self.energy <= 0:
                self.die()
            else:
                for i in range(0, self.mealsPerDay):
                    self.eat()
                if (self.energy >= self.energyNeededForBabies) and (self.age >= self.fertilityAge):
                    self.makeBabies()

             
    def die(self):
        # Color the animal's square green and remove it from the AnimalList
        # and from the NewAnimalList.
        board.setColor(self.row, self.col, "green")
        if self in AnimalList:
            i = AnimalList.index(self)
            del AnimalList[i]
        if self in NewAnimalList:
            i = NewAnimalList
            del NewAnimalList[i]
        
    def moveTo(self, row, col):
        # Move the animal to this new position, leaving its old position green.
        r = self.row
        c = self.col
        board.setColor(row, col, self.color)
        board.setColor(r, c, "green")
        self.row = row
        self.col = col
        
class Fox(Animal):
    # This represents one Fox
    count = 0
    def __init__(self, row, col):
        # The constructor initializes all of the attributes, and adds the
        # animal to the NewAnimalList and to the grid.
        self.color = "red"
        self.row = row
        self.col = col
        self.age = 0
        self.maxAge = 10
        self.fertilityAge = 4
        self.energy = 3
        self.oneYearEnergy = 2
        self.energyNeededForBabies = 2
        self.litterSize = 3
        self.mealsPerDay = 2
        NewAnimalList.append(self)
        board.add(self)
        Fox.count = Fox.count + 1
        reportFoxes()

    def oneYear(self):
        self.age = self.age + 1
        if self.numBunnyNeighbors() >= MachoBunnyFactor.get():
            self.die()
        if self.age > self.maxAge:
            self.die()
        else:
            self.energy = self.energy - self.oneYearEnergy
            if self.energy <= 0:
                self.die()
            else:
                for i in range(0, self.mealsPerDay):
                    self.eat()
                if (self.energy >= self.energyNeededForBabies) and (self.age >= self.fertilityAge):
                    self.makeBabies()

    def numBunnyNeighbors(self):
        numBunn = 0
        list = Neighbors(self.row, self.col)
        for entry in list:
            r = entry[0]
            c = entry[1]
            if board.isRabbit(r, c):
                numBunn = numBunn + 1

    def makeBabies(self):
        # This makes up to "litterSize" baby foxes.  The other limit is
        # the number of open squares around the current fox.   Since the
        # fox has just eaten "mealsPerDay" times, there should be some
        # open squares.  Note the call to random(); half the time this is
        # called it should return immediately with no new foxes.
        if (random() >= 0.5):
            return
        n = numberFreeNeighbors(self.row, self.col)
        if n > self.litterSize:
            litter = self.litterSize
        else:
            litter = n
        for i in range(0, litter):
            list = Neighbors(self.row, self.col)
            for entry in list:
                r = entry[0]
                c = entry[1]
                if board.isEmpty(r, c):
                    break;
            Fox(r, c)

    def eat(self):
        #This looks for a neighboring rabbit to eat.  If there is none
        # it takes a step in a random direction.
         list = Neighbors(self.row, self.col)
         foodPos = findRabbit(list)
         if foodPos != None:
             r = foodPos[0]
             c = foodPos[1]
             rabbit = FindInAnimalList(r,c)
             if rabbit != None:
                 rabbit.die()
                 self.moveTo(r, c)
                 self.energy = self.energy + rabbit.energy
         else:
            newPos = findEmpty(list)
            if  newPos != None:
                r = newPos[0]
                c = newPos[1]
                self.moveTo(r, c)

    def die(self):
        # This updates the fox count, then calls the usual Animal.die()
        # procedure.
        Fox.count = Fox.count - 1
        reportFoxes()
        Animal.die(self)
        
class Rabbit(Animal):
    # This represents one rabbit.
    count = 0
    def __init__(self, row, col):
        # The constructor initializes all of the attributes, and adds the
        # animal to the NewAnimalList and to the grid.
        self.color = "blue"
        self.row = row
        self.col = col
        self.age = 0
        self.maxAge = 18
        self.fertilityAge = 3
        self.energy = 2
        self.oneYearEnergy = 1
        self.energyNeededForBabies = 1
        self.energyFromFood = 3
        self.litterSize = 6
        self.mealsPerDay = 1
        NewAnimalList.append(self)
        Rabbit.count = Rabbit.count + 1
        reportRabbits()
        board.add(self)

    def makeBabies(self):
        # This makes up to "litterSize" baby rabbits.  The other limit is the
        # number of open squares around the current rabbit.  Note the call to
        # random(); half the time this is called it should return immediately
        # with no new rabbits.
        if (random() >= 0.5):
            return
        n = numberFreeNeighbors(self.row, self.col)
        if n > self.litterSize:
            litter = self.litterSize
        else:
            litter = n
        for i in range(0, litter):
            list = Neighbors(self.row, self.col)
            for entry in list:
                r = entry[0]
                c = entry[1]
                if board.isEmpty(r, c):
                    break;
            Rabbit(r, c)
        
    def eat(self):
        # If the rabbit can find an open square (presumably with grass)
        # it moves there and eats.  It should gain self.energyFromFood
        # units of energy if it finds the open square.
        list = Neighbors(self.row, self.col)
        foodPos = findEmpty(list)
        if foodPos != None:
            r = foodPos[0]
            c = foodPos[1]
            self.moveTo(r, c)
            self.energy = self.energy + self.energyFromFood
        
              
    def die(self):
        # This is the usual die() method that also updates the rabbit count.
        Animal.die(self)
        Rabbit.count = Rabbit.count - 1
        reportRabbits()

# _____________________________________________________________________

###                   UTILITY FUNCTIONS
         
def findRabbit(list):
    # Here "list" is a list of (row,column) positions.  This returns one
    # of these that holds a rabbit, if there is one.
    tempList = []
    for pos in list:
        row = pos[0]
        col = pos[1]
        color = board.getColor(row, col)
        if color == "blue":
            tempList.append(pos)
    num = len(tempList)
    if num == 0:
        return None
    else:
        n = (int)(random()*num)
        return tempList[n]

def findEmpty(list):
    # Here "list" is a list of (row,column) positions.  This returns one
    # of these that holds neither a fox nor a rabbit, if there is one.
    tempList = []
    for pos in list:
        row = pos[0]
        col = pos[1]
        color = board.getColor(row, col)
        if color == "green":
            tempList.append(pos)
    num = len(tempList)
    if num == 0:
        return None
    else:
        n = (int)(random()*num)
        return tempList[n]

def FindInAnimalList(row, col):
    # This looks through the AnimalList for an  entry that is at the
    # given (row, col) position
    for animal in AnimalList:
        if (animal.row == row)and (animal.col == col):
            return animal
    return None
            
def Neighbors(row, col):
    # This returns a list of all of the (row, column) positions that
    # are neighbors of the (row, col) argument.
    list = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i != row) or (j != col):
                if (i >= 0) and (i < board.rows) and (j >= 0) and (j < board.cols):
                        list.append( (i, j) )
    return list

def numberFreeNeighbors(row, col):
    # This counts the number of open neighbors of (row, col)
    count = 0
    list = Neighbors(row, col)
    for entry in list:
        r = entry[0]
        c = entry[1]
        if board.isEmpty(r, c):
            count = count + 1
    return count

def RandomlyPopulateGrid():
    # This randomly populates the grid.
    global GenerationNumber
    GenerationNumber = 0
    global InitialNumberRabbits
    global InitialNumberFoxes
#    InitialNumberRabbits = 200
#    InitialNumberFoxes = 20
    rabbits = InitialNumberRabbits
    foxes = InitialNumberFoxes
    for i in range(0, rabbits):
        while True:
            row = int(random()*board.rows)
            col = int(random()*board.cols)
            if board.isEmpty(row, col):
                Rabbit(row, col)
                break
    
    for i in range(0, foxes):
        while True:
            row = int(random()*board.rows)
            col = int(random()*board.cols)
            if board.isEmpty(row, col):
                Fox(row, col)
                break
    reportGenerations(GenerationNumber)
    
def AnimationLoop():
    # The usual function for animation
    global AnimalList, NewAnimalList
    global PAUSE
    global GenerationNumber
    for critter in AnimalList:
        critter.oneYear()
    for critter in NewAnimalList:
        AnimalList.append(critter)
        i = NewAnimalList.index(critter)
        del NewAnimalList[i]
    if len(AnimalList) == 0:
        PAUSE = True
        
    if (not PAUSE):
        GenerationNumber = GenerationNumber + 1
        reportGenerations(GenerationNumber)
        canvas.after(100, AnimationLoop)


    
def main():
    window = MyWindow()
    global AnimalList, NewAnimalList, PAUSE
    AnimalList = []
    NewAnimalList = []
    PAUSE = True
    global GenerationNumber
    GenerationNumber = 0
    
    global board
    board = Grid(30, 30, 15)
    AnimationLoop()
    canvas.mainloop()

main()
