input()
lis = map(int, input().split())

y = 0
m = 0

for i in lis:
    if i//30 >= 1:
        y += ((i//30)*10)+10
    else:
        y += 10

    if i//60 >= 1:
        m += ((i//60)*15)+15
    else:
        m += 15

if y == m:
    print(f"Y M {y}")
elif y < m:
    print(f"Y {y}")
elif y > m:
    print(f"M {m}")