import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

result_letters = ""
result_numbers = ""
result_symbols = ""
easy_password = ""
easy_password_list = []
hard_password = ""

for mr_letter in range(0, nr_letters, 1):
    result_letters = random.choice(letters)
    easy_password_list.append(result_letters)
    easy_password += result_letters

for nr_number in range(0, nr_numbers, 1):
    result_numbers = random.choice(numbers)
    easy_password_list.append(result_numbers)
    easy_password += result_numbers

for nr_symbol in range(0, nr_symbols, 1):
    result_symbols = random.choice(symbols)
    easy_password_list.append(result_symbols)
    easy_password += result_symbols


print(f"Your easy version password is : {easy_password}")

random.shuffle(easy_password_list) # List Data Shuffle (섞기)

for password in easy_password_list :
    hard_password += password

print(f"Your hard version password is : {hard_password}")



