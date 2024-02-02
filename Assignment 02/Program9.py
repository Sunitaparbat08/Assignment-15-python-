#Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character
#Input: char1 = ‘A’
#char2 = ‘C’
#Output: 132
#Input: char1 = ‘a’
#char2 = ‘b’

char1 = input("Enter the character1:")
char2 = input("Enter the Character2:")
a = ord(char1)
b = ord(char2)
if a%2!=0 and b%2!=0:
    add = a+b
    print(add)