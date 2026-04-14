_ = input()
lemons = input().replace(" ", "")
result = "Yes"

find_length = 0

while lemons != "":
    a = lemons.find("21")
    find_length = 2
    if a == -1:
        a = lemons.find("12")
        find_length = 2

    if a == -1:
        a = lemons.find("111")
        find_length = 3

    if a == -1:
        result = "No"
        break
    
    lemons = lemons[:a] + lemons[a+find_length:]

print(result)