fruits_tuples = [
    ('apple', 15),
    ('strawberry', 12),
    ('litchi', 10),
]

print(sorted(fruits_tuples, key = lambda fruits: fruits[1]))
