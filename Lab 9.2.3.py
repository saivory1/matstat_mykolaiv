s = input()
n = len(s)

if n == 1:
    print(1)
else:
    i = 0
    min_letters = 0

    while i < n:
        sub = s[i:]
        reversed_sub = sub[::-1]

        if sub == reversed_sub:

            min_letters = i
            break

        i += 1

    print(min_letters)