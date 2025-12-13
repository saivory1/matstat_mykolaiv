import matplotlib.pyplot as plt

vowels = "aeiou"

counts = {vowel: 0 for vowel in vowels}

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

for char in text:
    if char in vowels:
        counts[char] += 1

letters = list(counts.keys())
frequencies = list(counts.values())

plt.bar(letters, frequencies)
plt.xlabel("Голосні літери")
plt.ylabel("Частота появи")
plt.title("Частота появи голосних літер у тексті")

plt.savefig("vowels_histogram.png")

plt.show()