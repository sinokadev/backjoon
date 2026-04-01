while (i := input()) != "0 0":
    n, s = i.split()
    print("Yes" if int(n) > int(s) else "No")
