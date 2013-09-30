#This take numbers from the user and prints out the largest on exit

def main():
	done = False
	big = 0
	while not done:
		number = input("GIMMIE! ")
		if number > big:
			big = number
		if number == 0:
			done = True
			print ("the biggest one was %s") % big
main()