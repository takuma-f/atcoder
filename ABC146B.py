def main():
    alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    n = int(input())
    s = str(input())

    crypt = ""
    for c in list(s):
        crypt += alp[(alp.index(c) + n) % 26]

    print(crypt)


if __name__ == "__main__":
    main()
