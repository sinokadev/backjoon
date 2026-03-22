H, M = input().split()

time_minute = int(H)*60+int(M)

result = time_minute-45

if result//60 < 0:
    print(f"{24+(result//60)} {result%60}")
else:
    print(f"{(result//60)} {result%60}")