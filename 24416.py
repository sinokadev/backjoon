n = int(input())

resu1 = 0

def fib(n):
    global resu1
    if n == 1 or n == 2:
        resu1 += 1
        return 1
    else:
        return (fib(n-1) + fib (n-2))

fib(n)

resu2 = 0

def fibonacci(n):
    global resu2
    f = [1, 1]

    for i in range(3, n+1):
        resu2 += 1
        f.append(f[i-2]+f[i-3])
    
    return f[n-1]

fibonacci(n)
print(resu1, resu2)