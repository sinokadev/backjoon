a, b = input().split()

sa, sb = a[::-1], b[::-1]

print(max(int(sa), int(sb)))