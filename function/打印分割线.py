# 需求1打印一行分割线


def print_line():
    print("_" * 50)


print_line()


# 打印任意字符的分割线


def print_line_random(char):
    print(char * 50)


print_line_random("#")


# 需求3： 打印任意字符任意长度的分割线


def print_line_random_all(char, num):
    print(char * num)


print_line_random_all("^", 15)

# 打印多行分割线，并且满足上面的需求3


def print_lines(char, num, n):
    i = 0
    while i < n:
        print_line_random_all(char, num)
        i += 1


print_lines("h", 20, 3)
