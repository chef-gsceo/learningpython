from collections import Counter

marks = []

# вес оценок для сортировки
grade_weights = {
    "5+": 5.3,
    "5": 5.0,
    "5-": 4.7,

    "4+": 4.3,
    "4": 4.0,
    "4-": 3.7,

    "3+": 3.3,
    "3": 3.0,
    "3-": 2.7,

    "2": 2.0,
    "1": 1.0
}

# чтение файла
with open("MARKS", "r") as f:
    for line in f:
        if line.strip():
            topic, _, grade = line.split()

            marks.append((int(topic), grade))

# сортировка
sorted_marks = sorted(
    marks,
    key=lambda x: grade_weights.get(x[1], 0),
    reverse=True
)

# перезапись файла
with open("MARKS", "w") as f:
    for topic, grade in sorted_marks:
        f.write(f"{topic} - {grade}\n")

# вывод
print("=== По оценкам ===")
for topic, grade in sorted_marks:
    print(f"{topic} - {grade}")

# средняя оценка
avg = sum(grade_weights[g] for _, g in marks) / len(marks)

print(f"\nСредняя: {avg:.2f}")

# количество оценок
counts = Counter(g for _, g in marks)

print("\n=== Количество оценок ===")
for grade in sorted(counts):
    print(f"{grade}: {counts[grade]}")