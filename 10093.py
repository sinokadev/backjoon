a, b = map(int, input().split())
ans = range(min(a, b)+1, max(a, b))
print(len(ans))
print(*ans)
