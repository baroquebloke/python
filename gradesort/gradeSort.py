#Jacob Farnsworth

#This takes input from user in the form of names, takes user inputted grades in the form of numbers,
#and prints out the average grade per person and the list of grades, in formatted collums.

#I did not have much time to spend on this assignment and now i've forgotten to turn it in on time, 
#and so there are things I wish I could get it to do.
#for instance, I wish the columns would justify left, I wish the average grade would stop at just one decimal,
#and I cant seem to figure out how to get the names to print as part of the input prompt for the new_grade function.

#I could likely have worked these all out but time is not on my side.  Therefore, no bonus attempt on this either.  
#I would appreciate any thoughts on how this could have gone better.  Thanks!






def print_grades( gradebook ):
    print "%8s, %7s, %7s" %("name", "avg", "grades")
    for student in gradebook.keys():
        num = sum(gradebook[student])
        total = float(len(gradebook[student]))
        average = num / total
        print "%8s, %8s, %8s" %(student, average, gradebook[student])

def get_new_class_list( gradebook ):
    print "Enter class list:"
    while True:
        name = raw_input("name: ")
        if name == "":
            break
        elif name not in gradebook:
            gradebook[name] = []

def new_grade( gradebook ):
    names = gradebook.keys()
    names.sort()
    for student in names:
        print student                       ####this is driving me nuts...
        grade = input("grade: ")            ####
        gradebook[student].append(grade)
    
def main():
    gradebook = {}
    get_new_class_list( gradebook )
    while True:
        print "Command ('print', 'new', 'quit'): ",
        command = raw_input()
        if command == "quit":
            break
        elif command == "print":
            print_grades( gradebook )
        elif command == "new":
            new_grade( gradebook )

main()