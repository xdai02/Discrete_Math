def fibonacci(n):
    f = [0] * n
    f[0] = f[1] = 1
    for i in range(2, n):
        f[i] = f[i-2] + f[i-1]
    return f[n-1]

def main():
    n = 7
    print(fibonacci(n))

if __name__ == "__main__":
    main()