################################################################
#                                                              #
#    II.A. Алгоритм быстрого возведения в степень              #
#    II.B. Алгоритм быстрого возведения в степень по модулю    #
#                                                              #
################################################################


def fast_exponentiation_algorithm(a, n):
    # 1
    n = bin(n).split('b')[1][::-1]
    x = 1

    # 2
    for i, b_i in enumerate(n):
        x *= a ** (int(b_i) * (2 ** int(i)))

    # 3
    return x


def fast_exponentiation_algorithm_modulo(a, s, n):
    # 1
    nn = bin(s).split('b')[1][::-1]
    y = a
    b_0 = int(nn[0])
    x = a ** b_0

    # 2
    for i, b_i in enumerate(nn):
        if i == 0:
            continue

        y = (y ** 2) % n

        # 2.1
        if int(b_i) == 1:
            x = (x * y) % n

    # 3
    return x


if __name__ == "__main__":
    print(fast_exponentiation_algorithm(2, 3))
    print(fast_exponentiation_algorithm_modulo(2, 3, 9))
