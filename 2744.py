result = ""

for i in input():
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()

print(result)