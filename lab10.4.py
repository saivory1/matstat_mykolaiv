import numpy as np

a = np.array([9, 2, 0, 4])
b = np.array([5, 3, 7, 8])

print("Перший масив:", a)
print("Другий масив:", b)
print()

print("Додавання масивів:", a + b)
print("Віднімання масивів:", a - b)
print("Множення масивів:", a * b)
print("Ділення масивів:", a / b)
print()


c = np.concatenate((a, b))
print("Об'єднаний масив:", c)
print()

print("Максимальний елемент:", np.max(c))
print("Мінімальний елемент:", np.min(c))
print("Сума елементів:", np.sum(c))
print("Добуток елементів:", np.prod(c))