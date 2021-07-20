class MyClass: # class
    name1 = "abc" # variable
# creating functions inside of class 'def, is a keyword which is used for creating functions
# sum is fuction name
    def __init__(self,name,age):# first call this function init is inbuilt building function
        self.name=name
        self.age=age
    def sum(self,a,b): # self is a variable and its first argument in python
        print (a+b) # inside of function print statement
x=MyClass("defg",25) # x is variable for store object of class
print(x.name1)
x.sum(2,3) # call the function 2,3 are arguments are passing to a sum function
print(x.name)
print(x.age)


