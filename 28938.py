input()
a=map(int, input().split())

result = 0

for i in a:
    result += i

if result == 0:
    print("Stay")
elif result < 0:
    print("Left")
else:
    print("Right")