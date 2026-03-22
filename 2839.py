n = int(input())
tmp = n
result = 0
while True:
    if tmp == 0:
        break
    elif tmp < 0:
        result = -1
        break
    
    if tmp % 5 == 0:
        tmp -= 5 # 5kg을 가져가야함
    else:
        tmp -= 3
    result += 1

print(result)