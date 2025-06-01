#Creating and initializing variables
num=0

#Getting user inputs
num=int(input("Enter the number here:"))

#Process
if num<15:
    for i in range(0,num+1):
        print(i,end=" ")
else:
    for x in range(0,15):
        print(x,end=" ")