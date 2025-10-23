class Fraction:
    def __init__(self):
        self.n = 0
        self.d = 1

    def set_numerator(self, x):
        self.n = x

    def set_denominator(self, y):
        self.d = y

    def set_nd(self, x, y):
        self.n = x
        self.d = y

    def display(self):
        print(f"{self.n}/{self.d}")


def main():
    obj1 = Fraction()
    obj2 = Fraction()

    obj1.set_numerator(2)
    obj1.set_denominator(3)

    obj2.set_nd(5, 2)

    print("obj1: ", end='')
    obj1.display()
    print("obj2: ", end='')
    obj2.display()


if __name__ == '__main__':
    main()
