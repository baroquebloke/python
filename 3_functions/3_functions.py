#this program has three functions.  
#Function Length(x) returns the number of digits in integer x.  
#Function Power(a, b) returns a to the bth power, ie: a mutiplied by itself b times.
#Function Factorial(n), returns the factorial of n.


import math
# I found the math module in the python 2.7.5 online documentation.  
# The homework does not specify that we should use loops to calculate factorials, 
# only states that we can.  
# I prefer using the module over the loop.  
# I've included the loop commented out as well.
def Factorial(n):
	total = math.factorial(n)
	#total = 1
	#for number in range(2, n+1):
	#	total = total * number
	print "The factorial of %d is %d"  % (n, total)	
	return Length(total) 


def Power(a, b):
	total = 1
	for number in range(1, b+1):
		number = a * total
		total = number
	print "power(%d, %d) is %d" % (a, b, total)
	return Length(total)


def Length(x):
	number_of_digits = len(str(x))
	if number_of_digits <= 1:
		return "This has %d digit" % number_of_digits
	else:
		return "This has %d digits" % number_of_digits


#if enter/return is hit while anything other than a number is present in the text field, 
#the program crashes... Not sure what to do about this...
def main():
	done = False
	while not done:
		user_number = input("Enter a number, or 0 to exit: ")
		if user_number == 0:
			done = True
			print "goodbye!"
		elif user_number < 0:
			done = False
		else:
			print Factorial(user_number)
			print Power(user_number, user_number)

main()