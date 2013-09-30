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