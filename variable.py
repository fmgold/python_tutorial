#COMMENT
"""
VARIABLE 
Variable are container for storing data 
# Variable name should start with lower case char 
# digits are allowed but not at the start 
# underscore (_) is allow 
# are case sensitive 
"""


firstNumber = 3
secondNumber = 5
addition = firstNumber + secondNumber
#print(addition)

# id tell the memory location 
# type tell the datatype 

#printing type and id
#print(type(firstNumber), type(secondNumber))

#printing memory address 
#print(id(firstNumber),id(secondNumber))

#object intering i.e both variables are pointing to the same value 
a = 20 
b = 20 

#print(id(a),id(b))

#multiple variable 
x, y, z = "shola", "seun", "emmanuel"
#print(x)
#print(y)
#print(z)

names = ["lekan", "timilehin", "ruth"]
x,y,z = names 

#print(x,y,z)

#Global Variable 
occupation = "IoT Engineer"

def myWork():
	occupation = "Software Developer"
	print("My job role is",occupation)

#myWork()
#print("My job role is:", occupation) #Global Variable 


### DATATYPE 
# Integer as int 
firstNumber = 35

#print(firstNumber, type(firstNumber))

#float i.e decimal number 
c = 2.34 

#print(c, type(c), id(c))

#String 
#double quote
myName = "Joshua Kimmich "
#print(myName)

#single quote
myLastName = 'Cole Palmer'
#print(myLastName)

#tripple quote 
myCombinedName = """my lastname and first name are 
Joshua Kimmich and 
Cole Palmer"""
#print(myCombinedName)

#List 
myList = [100000, "laptop", "bigscreen", "Worktable", "Desklamp", 20 ]
#print(myList, type(myList), id(myList))
myList.append("shola")
#print(myList, type(myList), id(myList))

#tuple
myTuple = (20, 50, "seun")
#print(myTuple, type(myTuple))

#dictionary 
myData = {"name":"Shola Ayobami", "age": 25, "occupation": "Project Manager"}
#print(myData, type(myData))

#Set
mySet = {"Youghurt", "milk", "hollandia", 1000}
#print(mySet, type(mySet))

#Complex number 
complexNumb = 2j
#print(complexNumb, type(complexNumb))

#Range 
rang = range(6)
#print(rang)


##OPERATORS IN PYTHON 
#Arithmetic operators +, -, *, /, //, %, **

#num1 = 2
#num2 = 5

#print(num1 + num2)
#print(num1 - num2)
#print(num1 * num2)
#print(num1 ** num2)
#print(num2 / num1)
#print(num1 // num2)
#print(num1 % num2)

#Comparison operators <,>,<=, >=,==, != 

# numb1 = 100
# numb2 = 200
# print(numb1 < numb2)
# print(numb1 > numb2)
# print(numb1 <= numb2)
# print(numb1 >= numb2)
# print(numb1 != numb2)

#identity operators is and is not 

#num1 = 100
#num2 = 100

#print(num1 == num2)
#print(num1 == num2)
#print(num1 is num2)
# both variables are pointing to the same value and they have the same memory address

#l = [20,30,40]
#l2 = [20,30,40]
# both variables have the same dataset but different memory location 

#print(l == l2)
#print(l is not l2)

#Assignment Operators =, +=, =*
# number = 30
# number += 20
# print (number)

#Logical Operator and, or m not

# print(10==10 and 20 == 20)
# print(10==10 or 20 == 10)
# print(not(10==20))

#Membership operators 
# l = [10,20,30,50,45]
# print(30 in l)
# print(44 in l)

# s = "Python string"
# print("python" in s) # false 
# print("Python" in s) # true 

##CONDITIONAL STATEMENT 
# numb = 300
# numb2 = 200

# if numb > numb2 :
# 	print("number one is greater than number two")
# elif numb < numb2: 
# 	print("number one is lesser than number two")
# else :print("number one is equal to number two")


# if 1: #any non zero will be true 
# 	print("Statement in if block")
# else:
# 	print("State,emt om else block")


#FOR LOOP
# l = [1,2,3,4,5,20]
# sum = 0

# for value in l:
# 	sum = sum +value

# print(sum)

# for value in range(10,100):
# 	print(value)


# for value in range(10,100, 5):
# 	print(value)

# for value in range(20):
# 	print(value)

#print("Welcome to my computer game ")
playing = input("Do you wanna play? ")
print(playing)















