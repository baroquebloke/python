from random import *

class Dice:
    def __init__(self):
        self.values = [0, 0]

    def roll(self):
        # This sets self.values[0] and self.values[1] to random numbers between 1 and self.sides
        self.values[0] = randint(1, 6)
        self.values[1] = randint(1, 6)

    def doubles(self):
        # This returns True if the two dice values are equal
        if self.values[0] == self.values[1]:
            return True
        else:
            return False

    def total(self):
        # This returns the total of the two dice values
        dice_total = self.values[0] + self.values[1]
        return dice_total        

class Player:
    def __init__(self, myName):
        # In addition to self.next, this has instance variables self.name and self.total
        self.name = myName
        self.next = None  # don't change this
        self.total = 0
        
    def turn(self, dice):
        while True:
            dice.roll()
            x = dice.total()
            self.total = self.total + x
            print "   %s rolls %s for a total of %s" %(self.name, x, self.total)
            if dice.doubles():
                print "Doubles!!!"
                continue
            else:
                break
        # This has a loop that keeps rolling the dice and adding dice.total()
        # onto the player's total until dice.doubles() is False
        # So that the user can see what is going on, each time you roll the dice
        # print  the dice.total() and also the player's total.  The output will be
        # easier to read if you indent this information: print a few spaces at the start
        # of each line.
        # Remember to print the player's name with this so we can see who rolled the dice.
        # Altogether a typical line will be
        #       Bob rolls 7 for a total of 48
        

class Game:
    # You shouldn't need to change anything in this class
    def __init__(self, player0Name, player1Name, max):
        self.player0 = Player(player0Name)
        self.player1 = Player(player1Name)
        self.player0.next = self.player1
        self.player1.next = self.player0
        self.max = max
        self.dice = Dice()

    def play(self):
        # This has the players alternating turns until one gets at least self.max points
        done = False
        player = self.player0
        round = 0
        while not done:
            if player == self.player0:
                round = round + 1
                print "Round %d" % round
            player.turn(self.dice)
            if player.total >= self.max:
                done = True
                print "%s wins!!" % player.name
            player = player.next           
        print
        
def main():
    name1 = raw_input("Enter the first player: " )
    name2 = raw_input( "Enter the second player: " )
    goal = input( "Enter a goal for the game: " )
    G = Game(name1, name2, goal )
    G.play()
    
main()
