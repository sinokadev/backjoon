a = int(input())/4

if str(a).split(".")[1] == "0":
    print(f"{int(a)}.0")
else:
    print(f"{a:.2f}")