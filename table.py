names = ['abas', 'rusya', 'piro', 'gami']

for el in names:
    print(el.title())

message = "Warning, "
for el in names:
    print(message + el.title())
print("\tWarned", len(names), "people")

message = "Warning cancel"

names.insert(0, 'nina')
names.insert(3, 'lilit')
names.append('kiki')

for el in names:
    print(message, el.title())
print("\tWarned", len(names), "people")

print("Warning again")

message = "Sorry, for you warning again,  "
count = 0
while len(names) > 2:
    popped_name = names.pop()
    print(message + popped_name.title())
    count += 1
print("\tWarned", count, "people")


message = "No warning for you, "

for el in names:
    print(message + el.title())

while len(names) > 0:
    del names[0]

print(names)