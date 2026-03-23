length = int(input())
MAX_LEN = 50
words = []
words_index = [[] for _ in range(MAX_LEN)]

for _ in range(length):
    inp = input()
    if inp in words:
        continue
    words.append(inp)
    words_index[len(inp)-1].append(inp)

for i in range(MAX_LEN):
    words_index[i].sort()


print("---")

for i in words_index:
    for j in i:
        if j:
            print(j)
