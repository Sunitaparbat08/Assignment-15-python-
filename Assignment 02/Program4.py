# take a number from the user and check wheather it is present in list.if its in the list print "Available"
# list 1 = [10,20,30,40,50]
# "in" it is an membership operator in python that used to check wheather the any string or number is available in list or not 
# there are many way to check the number is list or not
# using loop(), using any function

list1 = [10,20,30,40,50]
num = int(input("Enter the Number:"))   
if num in list1:
    print("Available")
else:
    print("Not Available")    

'''# Using loop()
list1 = [10,20,30,40,50]
num = int(input("Enter the number:"))
for i in list1:
    if i<=50:
      print("yes")'''    

