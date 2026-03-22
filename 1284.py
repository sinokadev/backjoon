while True:
    inp = input()
    if inp == "0":
        break

    ans = 1
    for i in inp:
        if i == "0":
            ans += 4
        elif i == "1":
            ans += 2
        else:
            ans += 3
        ans += 1

    print(ans)
