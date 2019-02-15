def evaluate_arguments(*argv):
    args = []
    result = 1
    for arg in argv:
        try:
            int(arg)
            args.append(int(arg))
            result = result*int(arg)
        except:
            continue

    print(result)

evaluate_arguments() #Use your arguments to test :D