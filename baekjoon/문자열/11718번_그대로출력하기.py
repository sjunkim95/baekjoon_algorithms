for i in range(100):
    try:
        String = str(input())
        print(String)
    except EOFError:
        break
