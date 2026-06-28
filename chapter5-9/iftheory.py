cars = ['audi', 'bmw', 'subaru', 'toyota',]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')



# проверка вхождения в список
bannedusers = ['andrew', 'carolina', 'david']
user = 'mary'

if user not in bannedusers:
    print(f"{user.title()}, you are not banned.")

# ДЗ:
# Создать программу проверки данных пользователя.
# Использовать проверки строк, lower(), числовые сравнения,
# and/or, проверку наличия и отсутствия элементов в списке.

username = 'Chef'
userage = 23
userlangs = [
    'pascal',
    'basic',
    'c++',
    'python',
]

if username == 'Chef':
    print('true')
else:
    print('false')

if username.lower() == 'chef' and username.upper() == 'CHEF':
    print('true')
else:
    print('false')

if userage == 23:
    print('true')
else:
    print('false')

if userage != 24:
    print('true')
else:
    print('false')

if userage > 10:
    print('true')
else:
    print('false')

if userage < 30:
    print('true')
else:
    print('false')

if userage >= 23:
    print('true')
else:
    print('false')

if userage <= 23:
    print('true')
else:
    print('false')

if username == 'Chef' and userage >= 18:
    print('true')
else:
    print('false')

if username == 'Chef' and userage <= 18:
    print('true')
else:
    print('false')

if 'python' in userlangs:
    print('python is a userlang')
else:
    print('false')

if 'java' not in userlangs:
    print('Java is not a userlang')
else:
    print('false')

