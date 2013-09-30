def main():
	done = False
	exitString = raw_input("whats the exit string? ")
	while not done:
		question = raw_input("give me a string: ")
		if question == exitString:
			done = True
			print "Thats it!"
		else:
			done = False
			print "Nope"
main()