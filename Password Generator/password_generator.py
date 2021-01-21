# Defining Import
import random

# Creating Variables
lower_chars = 'abcdefghijklmnopqrstuvwxyz'
upper_chars = lower_chars.upper()
numbers = '1234567890'
other_char = "!@#$%&*()_+-=[]?"
chars = lower_chars+upper_chars+numbers+other_char

# Taking User Input
length = int(input('Password Length ? '))
passComb = int(input('Number Of Passwords ? '))

# Generating and Printing Passwords
for pwdOptions in range(passComb):
    password = ''
    for pwd in range(length):
        password += random.choice(chars)
    print(password)

