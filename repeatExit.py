def main():
	done = False
	clue = raw_input("String: ")
	while not done:
		hint = raw_input("String: ")
		if hint == clue:
			done = True
		else:
			clue = hint
main()