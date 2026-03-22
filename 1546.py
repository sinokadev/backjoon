length = int(input())
inp = list(map(int, input().split()))

M = max(inp)

newgrade = [i/M*100 for i in inp]

print(sum(newgrade)/length)
