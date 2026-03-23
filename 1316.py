def isgroup(text: str):
    end = [False for _ in range(26)]

    for i in range(len(text)-1):
        if end[ord(text[i])-97]:
            return False
        
        if text[i] != text[i+1]:
            end[ord(text[i])-97] = True
    
    if end[ord(text[-1])-97]:
        return False

    return True

result = 0

for i in range(int(input())):
    if isgroup(input()):
        result += 1

print(result)