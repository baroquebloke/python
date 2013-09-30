#this plays blackjack with the user.  
#It gives the user a number and if the number is less than 21, asks the user if they would like another.  

from random import*
def main():
	total = 0
	done = False
	while not done:
		cmd = raw_input("Would you like to play? yes or no: ")
		if cmd == "yes":
			num = randint(1, 11)
			total = total + num
			print "your new number is %s" % num
			print "you now have %s" % total
		if total >= 18 and total in range(18, 22):
			done = True
			print "YOU WIN"
		if total > 21:
			done = True
			print "BUST! YOU LOST"
		if cmd == "no" and total < 18:
			done = True
			print "QUITTER! YOU LOSE!!"
		elif cmd == "no" and total in range(18, 22):	
			done = True
			print "HUZZAH! YOU WIN!!"
main()