#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ""
while nr_letters or nr_numbers or nr_symbols:
    choice = random.choice([letters if nr_letters > 0 else 0, numbers if nr_numbers > 0 else 0, symbols if nr_symbols > 0 else 0])

    if choice == letters:
        key = random.choice(letters)
        nr_letters-=1
    elif choice == numbers: 
        key = random.choice(numbers)
        nr_numbers-=1
    elif choice == symbols:
        key = random.choice(symbols)
        nr_symbols-=1
    elif choice == 0:
        continue
    else:
        print("Error")
        break

    password += key 

print(password)