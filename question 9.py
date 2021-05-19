#Name: Leon Chen
#Date: May 13
#This program calculated the sum of the digits of a number

#input data
number=int(input("Enter a positive integer:"))

#process data
sum=0
while number>0:
    digit=number%10
    sum=sum+digit
    number=number//10

#output data
print("The sum of the digits is", sum)
    
