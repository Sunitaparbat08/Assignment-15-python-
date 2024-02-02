# Take two numbers from the user, check if both are odd and then print the sum of the numbers.
#Input: num1 = 10
#Input: num2 = 11
#Output: 21
#Input: num1 = 10
#Input: num2 = 6
#Output: No Output

num1 = int(input("Enter the Number1 :"))
num2 = int(input("Enter the Number 2 :"))
if num1%2!=0 or num2%2!=0:
    add = num1+num2
    print(add)
else:
    print("No output")    