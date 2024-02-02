#Take Two character from user check if the ascii value both of character are odd then print the sum of ascii values of character
#Input: char1 = ‘A’
#char2 = ‘C’
#Output: 132
#Input: char1 = ‘a’
#char2 = ‘b’

char1 = input("Enter the character1:")
char2 = input("Enter the Character2:")
if ord(char1)%2!=0 and ord(char2)%2!=0:
    add = char1+char2
    print(add)