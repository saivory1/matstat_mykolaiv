A = [4, 2, 0, 3, 6, 7, 9, 2]

print("Список A:", A)


if 0 in A:
    index_zero = A.index(0)
    total = 0


    for x in A[index_zero + 1:]:
        if x % 2 != 0:
            total += x

    print("Сума непарних елементів після першого нуля:", total)
else:
    print("У списку немає нульового елемента")