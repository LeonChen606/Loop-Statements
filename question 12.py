#Name: Leon Chen
#Date: May 13
#This program finds the greatest common factor of 2 numbers

#input data
number1=int(input("Enter a postive number:"))
number2=int(input("Enter another positive number:"))

#finding the GCF
while number2>0:
    temp=number1%number2
    number1=number2
    number2=temp

#output data
print("The greatest common factor is", number1)

