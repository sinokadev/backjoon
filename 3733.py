while True:
    try:
        n, s = input().split()
        print(int(s)//(int(n)+1))
    except EOFError:
        break