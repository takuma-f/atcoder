def main():
    a, b, x = map(int, input().split())
    n = 0

    while x > (a*n)+(b*len(str(n))):
        n += 1
    else:
        print(n-1 if n < 0 else 0)
        exit()


if __name__ == "__main__":
    main()
