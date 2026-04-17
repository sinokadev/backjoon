a, b = input().split()
c, d = input().split()

e, f = int(a)+int(c), int(b)+int(d)

if e == f:
    print("Either")
elif e < f:
    print("Hanyang Univ.")
else:
    print("Yongdap")