# развертка генераторов списков (внутреннее устройство)

x = [i for i in range(5)]
print(x)

x = []
for ii in range(5):
    x.append(ii)
print(x)


print("\n########")


x = [i ** 3 for i in range(5)]
print(x)

x = []
for ii in range(5):
    x.append(ii ** 3)
print(x)


print("\n########")


x = [i for i in range(5) if i % 2 == 0]
print(x)

x = []
for ii in range(5):
    if ii % 2 == 0:
        x.append(ii)
print(x)

print("\n########")
print("ДЗ")
print("########")

# ДЗ: вывести первые 3, 3 из середины, и 3 последние элементы списка используя срез списков

digitz = [3, 6, 78, 45, 34, 456, 23, 23445, 234, 2452, 234546534, 6543, 46, 3, 55, 1]
print(digitz)

print("\nFirst 3 digits")
print(digitz[:3])

print("\nMiddle 3 digits")
print(digitz[5:8])

print("\nLast 3 digits")
print(digitz[-3:])

# ДЗ: скопировать список пиццы, добавить новую пиццу в исходный список, добавить другую пиццу
# во второй список новый, доказать что существуют два разных списка после копирования
# вывести через цикл for первый список пиццы, затем так же второй список пиццы

pizza = ['pineapple', 'pepperonni', 'margarita']
newpizza = pizza[:]

pizza.append('tomatto')
newpizza.append('olivian')

print('\nFirst list:')
for el in pizza:
    print(el)

print('\nSecond list:')
for el in newpizza:
    print(el)
