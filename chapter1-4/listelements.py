names = ['abas', 'rusya', 'piro', 'gami']
modetype = (input("select mode: "))
modetype = int(modetype)

if modetype == 1:
    print(names[0].title())
    print(names[1].title())
    print(names[2].title())
    print(names[3].title())

    message = "Warning"

    print(message, names[0].title())
    print(message, names[1].title())
    print(message, names[2].title())
    print(message, names[3].title())

    names[0] = 'oboz'
    print(message, names[0].title())

    names.append('lixo')
    names.insert(0, 'ohi')
    print(names)

    del names[5]
    print(names)

    popped_name = names.pop()
    print(names)
    print(popped_name.title())

    popped_name2 = names.pop(3)
    print(f"Last name is {popped_name2.title()}.")

    names.remove('ohi')
    print(names)

    not_needed = 'oboz'
    names.remove(not_needed)
    print(names)
    print(f"\nA {not_needed.title()} is not needed")
elif modetype == 2:
    message = "Hi, "
    print(message, names[0].title())
    print(message, names[1].title())
    print(message, names[2].title())
    print(message, names[3].title())

    can_not_come = "piro"
    names.remove(can_not_come)
    names.insert(3,'kula')
    print(names)