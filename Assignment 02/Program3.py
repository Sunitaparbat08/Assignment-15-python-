# WAP Take a two numbers from users and print of those number if the sum is even

num1 = int (input("Enter the number 1:"))
num2 = int(input("Enter the Number 2:"))
num = num1+num2
if(num%2==0):
    print(num,"is even")
else:
    print("No output")    