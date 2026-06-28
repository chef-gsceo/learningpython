# list преобразует в список
numbers = list(range(1, 6))
print(numbers)


# четные с шагом 2       2-начало 11-конец 2-шаг
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)

print(squares)


# тоже самое как с четными
squares = []
for i in range(1, 11):
    squares.append(i ** 2)

print(squares)


# функции числовых списков (сумма, минимальное число и максимальное число)
values = []
for i in range(10):
    values.append(i)

print(values)
print(min(values))
print(max(values))
print(sum(values))

# генерация списка короткий формат
squares = [value ** 2 for value in range(1,11)]
print(squares)

# ДОМАШНЕЕ ЗАДАНИЕ
# task 1: используйте цикл for для вывода чисел от 1 до 20 включительно
#task 1 v1
for i in range(1, 21):
    print(i)

# task 1 v2
nums = [i for i in range(1, 21)]
print(nums)


# task 2: создайте список от 1 до 1000000, используйте цикл for для вывода чисел(интеррапт если будет слишком долго)
nums = [i for i in range(1, 1000001)]
print(nums)
# я не понял зачем тут цикл for если уже есть список но окей
nums = []
for i in range(1, 1000001):
    nums.append(i)

print(nums)
