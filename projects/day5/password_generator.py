#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level COMPLETE - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []

for i in range(nr_letters):
    #print(random.choice(letters), end = "")
    password.append(random.choice(letters))

for i in range(nr_symbols):
    #print(random.choice(symbols), end = "")
    password.append(random.choice(symbols))

for i in range(nr_numbers):
    #print(random.choice(numbers), end = "")
    password.append(random.choice(numbers))

password_output = ''.join(password)
print("Easy: " + password_output)

#Hard Level COMPLETE  - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

print("Hard: " + ''.join(random.sample(password_output,len(password_output))))