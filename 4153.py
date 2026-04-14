while True:
    a = sorted(list(map(int, input().split())), reverse=True)
    if a[0] == a[1] == a[2] == 0:
        break

    print("right" if a[0]**2 == a[1]**2 + a[2]**2 else "wrong")