a = int(input())
b = int(input())

k = (b - a + 1000) // 1001

result = a + (b - a) * k

print(result)