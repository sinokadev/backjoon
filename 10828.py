stack = []
for i in range(int(input())):
    command = input()

    if command.startswith("push"):
        stack.append( int(command.split()[1]))
    elif command == "pop":
        if len(stack) != 0:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command == "top":
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)