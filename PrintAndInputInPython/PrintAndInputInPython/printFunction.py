print() # result ()
print("Hello World") #result Hello World
print("Hello " *3) # result Hello Hello Hello 
print("All the power \n is with in you ") # All the power 
# is with in you 

a,b=10,20
print(a,b) # result (10, 20)
print(a+b) # result 30

#string

name="John"
marks=94.5
print(name,marks) #result ( John 94.5)
print("name,marks") # result name,marks
print("name is",name,"marks are",marks) # result ('name is', 'John', 'marks are', 94.5)
print("name is %s,marks are %f" %(name,marks)) # results name is John,marks are 94.500000
print("name is %s,marks are %.2f" %(name,marks)) # result name is John,marks are 94.50, %.2f is to display 2 numbers after the decimal number 
print("Name is {},Marks are {}".format(name, marks)) # result Name is John,Marks are 94.5
print("Name is {0},Marks are {1}".format(name, marks)) #result Name is John,Marks are 94.5

# %i for integer data 
# %f for floating point data 
# %s for string data 