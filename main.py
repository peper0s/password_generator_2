import random

print('Это программа генерации паролней')

password_keys = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_numbers = int(input("введите длину пароля"))

password = ""

for i in range(password_numbers):
    letter = random.choice(password_keys)
    password += letter
print(password)