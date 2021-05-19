#Name: Leon Chen
#Date: May 13
#This project calculated the sum of the cubes of the digits of a number

#input data
number=int(input("Enter a positive integer:"))

#finding each digit and cubing it
sum=0
while number>0:
    digit=number%10
    digit=digit**3
    sum=sum+digit
    number=number//10

#output data
print("The sum of the cubes of the digits is", sum)
    
