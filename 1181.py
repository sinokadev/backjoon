length = int(input())
MAX_LEN = 50
words = []

for _ in range(length):
    inp = input()
    words.append(inp)

words_two = list(set(words))

words_two.sort(key=lambda x: (len(x), x))

for i in words_two:
    print(i)
