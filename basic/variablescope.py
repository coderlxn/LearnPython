total = 0


def sum_(arg1, arg2):
    global total
    total = arg1 + arg2
    print("inner : ", total)
    return total


def outer():
    num = 10

    def inner():
        nonlocal num
        print(num)
        num = 100
        print(num)
    inner()
    print(num)


outer()


sum_(10, 20)
print("outer : ", total)
