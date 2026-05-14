import random

target = random.randint(1, 50)

print("Угадай число от 1 до 50! Да начнется игра!")
name = input("Введи имя: ")
more = "Не угадал! Слишком много!"
less = "Не угадал! Слишком мало!"
attempts = 0

while True:
    guess = int(input("Угадай число: "))
    attempts += 1
    if guess > target:
        print(more)
    elif guess < target:
        print(less)
    else:
        break

print(f"{name.title()}, поздравляю! Ты отгадал число за {attempts} шагов!")