for _ in range(int(input())):
    n = int(input())

    if n == 1:
        print(1)
    else:
        a = [1, 1, 1, 2, 2]

        for i in range(5, n):
            a.append(a[i-1]+a[i-5])

        print(a[n-1])