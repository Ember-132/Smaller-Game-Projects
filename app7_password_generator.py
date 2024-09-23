import random

print("Welcome to the PyPassword Generator!")

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols would you like? "))
number_of_numbers = int(input("How many numbers would you like? "))

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p","q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols_list = ["{", "}", "#", ",", "!", "_", "@", "/", "^", "?", "%", "&", "$", "(", ")", "£", "-"]
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8" , "9"]

random_letters = random.choice(letters_list)

for letter in letters_list:
    if len(random_letters) == number_of_letters:
        break
    else:
        random_letters += random.choice(letters_list)

random_symbols = random.choice(symbols_list)

for symbol in symbols_list:
    if len(random_symbols) == number_of_symbols:
        break
    else:
        random_symbols += random.choice(symbols_list)

random_numbers = random.choice(numbers_list)

for number in numbers_list:
    if len(random_numbers) == number_of_numbers:
        break
    else:
        random_numbers += random.choice(numbers_list)

first_iteration = random_letters + random_symbols + random_numbers

#we then have to randomise the characters in the first iteration above

first_random_letter = random.choice(first_iteration)

for item in first_iteration:
    if len(first_random_letter) == len(first_iteration):
        break
    else:
       first_random_letter += random.choice(first_iteration)

print(f"Your new password is: {first_random_letter}")