for i in range(int(input())):
    result = ""
    num, inp = input().split()
    for j in inp:
        result += j*int(num)
    
    print(result)