import random
import string

chars = []
special_characters = "!@#$%&*()/"

while True:
    try:
        pass_length = int(input("Please enter the length of the password: "))
        if pass_length == 0:
            print("Password can not have 0 characters!")
            continue
        elif pass_length < 0:
            print("Enter a positive integer!")
            continue
        break
    except:
        print("Invalid length")

chars.append(random.choice(string.ascii_lowercase))
chars.append(random.choice(string.ascii_uppercase))
chars.append(random.choice(string.digits))
chars.append(random.choice(special_characters))

for i in range(0,pass_length - 4):
    letter = random.choice(string.ascii_letters + string.digits + special_characters)   # string.punctuation
    chars.append(letter)

random.shuffle(chars)
password = ''.join(chars)
print(password)



