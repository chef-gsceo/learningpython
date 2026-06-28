# pizza
pizza = ['pepperoni', 'chicken', 'italian']
message_hate = 'Actually I hate pizza.'
message_like = 'I like pizza'

for el in pizza:
    print(f"{message_like} {el.title()}.")

print(message_hate)


# animals
animals = ['cat', 'dog', 'rabbit', 'fish']
message = 'is a great household animal.'
global_message = 'All of them are great household animals.'

for el in animals:
    print(f"{el.title()} {message}")

print(global_message)
