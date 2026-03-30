S1, S2 = input().split()
N1, N2 = input().split()
U1, U2 = input().split()

def get_gasungbe(one, two):
    a = (two*10)
    b = one*10
    if b >= 5000:
        b -= 500
    return a/b

sg = get_gasungbe(int(S1), int(S2))
ng = get_gasungbe(int(N1), int(N2))
ug = get_gasungbe(int(U1), int(U2))

maxg = max(sg, ng, ug)

if maxg == sg:
    print("S")
elif maxg == ng:
    print("N")
elif maxg == ug:
    print("U")