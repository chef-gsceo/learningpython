progs = ['apt', 'nginx', 'bash', 'kernel', 'python', 'vscode', 'git']

before = "\t\nBefore changes:"
deleted = "\t\nAfter delete:"
added = "\t\nAfter addition:"
after_sort = "\t\nAfter sort:"
after_sorted = "\t\nAfter sortED:"


# функции вывода списка после изменений
def show_progs(message, progs):
    print(message)

    for el in progs:
        print(el.title())


# выводим список до изменений
show_progs(before, progs)

# добавляем две строки
progs.append('ufw')
progs.insert(0, 'systemd')

# выводим список после добавления
show_progs(added, progs)

# удаляем элемент - del по индексу
del progs[3]

# выводим список после удаления
show_progs(deleted, progs)

# удаляем последний с конца элемент - pop через переменную
popped_prog=progs.pop()
print(f"Deleted: {popped_prog}")

# выводим список после удаления
show_progs(deleted, progs)

# удаляем элемент - remove по значению
progs.remove('apt')

# выводим список после удаления
show_progs(deleted, progs)

# сортируем список sorted (список останется в том же порядке)
sorted_progs = sorted(progs)

# выводим список после сортировки
show_progs(after_sorted, sorted_progs)

# сортируем в реверс sorted (список останется в том же порядке)
revsorted_progs = sorted(progs, reverse=True)

# выводим список после сортировки
show_progs(after_sorted, revsorted_progs)

# сортируем НАВСЕГДА sort
progs.sort()

# выводим список после сортировки
show_progs(after_sort, progs)

# сортируем в реверс sort НАВСЕГДА
progs.sort(reverse=True)

# выводим список после сортировки
show_progs(after_sort, progs)

# сортируем В ДАННОМ КОДЕ обратно как обычно (убывание) sort НАВСЕГДА
# стандартно - это РЕВЕРС, поскольку ранее в данном коде уже былабыла
progs.sort(reverse=True)

# выводим список после сортировки
show_progs(after_sort, progs)

# считаем оставшиеся элементы списка len
print(len(progs))
