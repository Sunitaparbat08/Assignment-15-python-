#Take single character from user check if the ascii value of character is Even the print character.
#Input char1 = ‘B’
#Output: B
#Input char1 = ‘C’
#Output: No Output

char = input("Enter the Character:")
if ord(char)%2 == 0:
    print("yes")
else:
    print("No Output")  