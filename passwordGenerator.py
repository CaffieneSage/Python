#My attempt at a password creator for Dr. Angela Yu's 100 days of code python bootcamp.
#First we import the randomness.
import random

#Get how many characters we need from the user.
print("How many characters?")
charsIn = int(input())


#Define a list of possible characters.
ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A',
     'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', '$', '%',
     '@', '#', '&']

#Create an empty string to store our password.
password = ""

#Loop through the character list the amount of times stated by the user
#then concatenate the result with the previous iteration.
for char in range(1, charsIn+1):
    select = random.choice(ch)
    password = password + select 

#output the password.
print(password)
