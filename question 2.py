#Name: Leon Chen
#Date: May 17
#This program asks the user to input a bunch of numbers and calculates the sum of all even numbers, the product of all positive numbers, and the number of numbers between -5 and 5

#input data
number=int(input("Enter the amount of numbers you would like to input:"))
print("\nMake sure the numbers you input are less that 100 and gretaer than -100.")
counter=1
positiveCount=0
product=1
sum=0

#inputting the numbers and deciding which category the land under
while counter<=number:
    value=int(input("Enter number %d:"% (counter)))
    if value>0:
        product=product*value
    if value>=-5 and value<=5:
        positiveCount=positiveCount+1
    if value%2==0:
        sum=sum+value
    counter=counter+1
    
#output data
print("The sum of all even numbers is", sum)
print("The product of all positive numbers is", product)
print("There are", positiveCount,"numbers between -5 and 5 including")
        
