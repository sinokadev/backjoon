n, a, b = map(int, input().split())

c = b-n + n

if c == a:
    print("Anything")
if c > a:
    print("Bus")
if c < a:
    print("Subway")