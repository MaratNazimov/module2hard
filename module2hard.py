import random

numbers = random.randint(3, 20)

password = ''
for i in range(1, 21):
    for j in range(i + 1, 21):
        if numbers % (i + j) == 0:
            if i == j:
                continue
            password = password + str(i) + str(j)

print(numbers)
print(password)
