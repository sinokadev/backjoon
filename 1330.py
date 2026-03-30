inp, inp2 = input().split()

if int(inp) < int(inp2):
    print("<")
elif int(inp) > int(inp2):
    print(">")
elif int(inp) == int(inp2):
    print("==")