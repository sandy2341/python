# simple calculator python program by using if-else statement
# creating 3 variables one is for 1st no,second is for operator, third one is for 2nd no
a=int(input("Enter a 1st number = "))
print("Select Operator You want to perform\n 1 for Addition\n 2 for Subtraction\n 3 for Multiplication\n 4 for Division ")
b=int(input("Select Operator\n"))
c=int(input("Enter 2nd Number = "))

if (b==1) :
    print("Your Answer is ",a+c)
elif (b==2) :
    print("Your Answer is ",a-c)
elif (b==3):
    print("Your answer  ",a*c)
elif (b==4) :
    print("Your Answer is ",a/c)
else :
    print("You have Entered Invalid Input please try again")
