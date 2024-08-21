import random 
simvols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
simvols1 = int(input("Какой длины пароль вам нужен?"))
password = ""
for i in range(simvols1):
    password += random.choice(simvols)
print(password)


