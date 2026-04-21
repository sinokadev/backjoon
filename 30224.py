a = int(input())

if (not "7" in str(a)) and a%7 != 0:
    print(0)
elif (not "7" in str(a)) and a%7 == 0:
    print(1)
elif "7" in str(a) and a%7 != 0:
    print(2)
elif "7" in str(a) and a%7 == 0:
    print(3)