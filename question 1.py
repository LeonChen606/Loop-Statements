#Name: Leon Chen
#Date: May 17
#This program calculates the average of a user's marks

#input data
sum=1
counter=1
course=int(input("Enter the amount of courses you like to enter:"))

#inputting all the marks and calculating the average
while counter<=course:
    mark=int(input("Enter the mark of course %d:"% (counter)))
    sum=sum+mark
    counter=counter+1
average=sum/course 

#output data
print("The average mark of all the inputted courses is %.1f"% average)
