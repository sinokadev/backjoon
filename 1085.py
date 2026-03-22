x, y, w, h = map(int, input().split())

result = min(
    abs(w-x),
    abs(h-y),
    x,
    y
)

print(result)