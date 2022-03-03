def factorial(n):
    # base case (기저 사례)
    if n <= 0:  # 1
        return 1
    return n*factorial(n-1)


if __name__ == "__main__":
    for i in range(1, 6):
        print(factorial(i))  # 2
