n = int(input())

for i in range(n):
    ai, bi, xi = input().split()

    print(int(ai)*(int(xi)-1)+int(bi))