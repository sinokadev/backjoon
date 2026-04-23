n = int(input())

if n == 1:
    print(1)
else:
    a = [1, 2]

    for i in range(3, n+1):
        a.append((a[0]+a[1])%15746)
        a.pop(0)

    print(a[-1])