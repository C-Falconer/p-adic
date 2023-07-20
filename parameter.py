def handle(argv, *args):
    args = list(args)
    for i in range(len(args)):
        inting = False
        if isinstance(args[i], tuple) or isinstance(args[i], list):
            inting = args[i][1]
        if len(argv) > i + 1 and inting:
            args[i] = int(argv[i + 1])
        elif len(argv) > i + 1:
            args[i] = argv[i + 1]
        else:
            break
    for j in range(i, len(args)):
        if isinstance(args[j], tuple) or isinstance(args[j], list):
            args[j] = args[j][0]
    if len(args) == 1:
        args = args[0]
    return args

if __name__ == "__main__":
    print("Program for handling input parameters")
