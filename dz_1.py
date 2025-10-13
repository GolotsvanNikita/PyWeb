def display_nums(a, b):
    if a < b:
        r = range(a, b + 1)
        print(*r)
    elif a > b:
        r = reversed(range(b, a + 1))
        print(*r)
    else:
        print(a)


def main():
    num1 = int(input("enter num1: "))
    num2 = int(input("enter num2: "))
    display_nums(num1, num2)


if __name__ == '__main__':
    main()
