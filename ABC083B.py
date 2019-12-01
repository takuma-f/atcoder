def main():
    input_list = list(map(int,input().split()))

    n = input_list[0]
    a = input_list[1]
    b = input_list[2]

    answer = 0
    for i in range(1, n+1):
        digit_sum = sum(list(map(int, str(i))))
        if (digit_sum >= a) and (b >= digit_sum):
            answer += i

    print(answer)

if __name__ == "__main__":
    main()
