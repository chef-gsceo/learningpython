names = ['abas', 'rusya', 'piro', 'gami']

for el in names:
    print(el.title())

message = "Warning, "

for el in names:
    print(message + el.title())
print(len(names))

message = "Warning cancel"

names.insert(0, 'nina')
names.insert(3, 'lilit')
names.append('kiki')

for el in names:
    print(message, el.title())
print(len(names))
print("Warning again")

message = "Sorry, "

while len(names) > 2:
    popped_name = names.pop()
    print(message + popped_name.title())


message = "No warning for you, "

for el in names:
    print(message + el.title())

while len(names) > 0:
    del names[0]

print(names)