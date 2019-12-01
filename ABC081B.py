def isEven(num):
    return num % 2 == 0

def main():
    n = int(input())
    num_list = list(map(int,input().split()))
    count = 0
    while True:
        for i in range(n):
            if isEven(num_list[i]):
                num_list[i] = num_list[i] / 2
            else:
                print(count)
                exit()
        count += 1

if __name__ == "__main__":
    main()