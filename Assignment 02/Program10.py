#Take the number from user and modulus with 8 if the reminder of the number is 3 then print reminder.
#Input num = 27
#Output: 3
#Input: num = 10
#Output: No Output

num = int(input("Enter the Number:"))
a = num%8
if a==3:
    print(a)
else:
    print("No output")    