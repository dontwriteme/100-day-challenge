import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']
print('Password generator:')
letters_quantity = int(input('How many letters would you like in your password?\n'))
symbols_quantity = int(input('How many symbols would you like?\n'))
numbers_quantity = int(input('How many numbers would you like?\n'))

password = []

for i in range(letters_quantity):
    random_index = random.randrange(len(letters))
    password += letters[random_index]

for i in range(symbols_quantity):
    random_index = random.randrange(len(symbols))
    password += symbols[random_index]

for i in range(numbers_quantity):
    random_index = random.randrange(len(numbers))
    password += numbers[random_index]

random.shuffle(password)

string_password = ''
for i in password:
    string_password += i
print(string_password)