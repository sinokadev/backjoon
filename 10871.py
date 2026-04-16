n, x = input().split()
mylist = input().split()
x=int(x)
result = []
for i in mylist:
    if int(i) < x:
        result.append(int(i))
    
print(*result)