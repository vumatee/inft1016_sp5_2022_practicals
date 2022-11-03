import random
import string

password = ""
length = int(input("How long should the password be?: "))

for char in range(length):
    letters = random.choice(string.ascii_letters)
    password += letters

print("Your randomly generated password is:", password)