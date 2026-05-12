for i in range(100000000):
    num = float(input())
    if num >= 0:
        result = num * 2
        print(f"Result: {result:.2f}")
    else:
        print(f"Negative number!")
        break
