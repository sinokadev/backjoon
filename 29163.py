input()
a=map(int, input().split())

re = 0

for i in a:
    if i%2 == 0:
        re += 1
    else:
        re -= 1

if re > 0:
    print("Happy")
else:
    print("Sad")