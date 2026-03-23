inp = input()
ispass = False
ispass2 = False
result = 0

for i in range(len(inp)):
    if ispass2:
        ispass = True
        ispass2 = False
        continue
    if ispass:
        ispass = False
        continue
    
    try:
        if inp[i] == "c" and inp[i+1] == "=":
            ispass = True
        elif inp[i] == "c" and inp[i+1] == "-":
            ispass = True
        elif inp[i] == "d" and inp[i+1] == "z" and inp[i+2] == "=":
            ispass2 = True
        elif inp[i] == "d" and inp[i+1] == "-":
            ispass = True
        elif inp[i] == "l" and inp[i+1] == "j":
            ispass = True
        elif inp[i] == "n" and inp[i+1] == "j":
            ispass = True
        elif inp[i] == "s" and inp[i+1] == "=":
            ispass = True
        elif inp[i] == "z" and inp[i+1] == "=":
            ispass = True
    except IndexError: pass

    result += 1

print(result)