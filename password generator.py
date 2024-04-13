
import random 
import string 


letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation


letter_num = int(input('How many letters would you like in your password? '))
number_num = int(input('How many numbers would you like in your password? '))
special_num = int(input('How many special characters would you like in your password? '))


password = ''
for i in range(letter_num):
    password += random.choice(letters)
for i in range(number_num):
    password += random.choice(numbers)
for i in range(special_num):
    password += random.choice(special_chars)


password = ''.join(random.sample(password, len(password)))

print('Password: ' + password)