#this takes numbers from the user and prints the sum on exit

def main():
	done = False
	count = 0
	while not done:
		number = input("GIMMIE! ")
		count = number + count
		if number == 0:
			done = True
			print ("the sum was %s") % count
main()