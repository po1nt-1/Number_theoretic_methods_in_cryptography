#######################################
#                                     #
#    III. Вычисление символа Якоби    #
#                                     #
#######################################


from main import Error


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def calculate_Jacobi_symbol(a, n):
    if not isinstance(a, int):
        raise Error("Некорректные входные данные")
    if not isinstance(n, int) and not isinstance(n, float):
        raise Error("Некорректные входные данные")
    if n % 2 == 0 or n < 3 or a < 0 or a >= n:
        raise Error("Некорректные входные данные")

    if NOD(int(a), int(n)) != 1:
        return 0
    if n == 1 or n == -1:
        return 1

    # 1
    g = 1
    # 2
    while True:
        # 3
        if a == 0:
            return 0
        if a == 1:
            return g
        # 4
        k = 0
        a_1 = a
        while a_1 % 2 == 0:
            a_1 /= 2
            k += 1
        # 5
        s = 1  # if k % 2 == 0
        if k % 2 != 0:
            if n % 8 == 1 or n % 8 == -1:
                s = 1
            elif n % 8 == 3 or n % 8 == -3:
                s = -1
        # 6
        if a_1 == 1:
            return g * s
        # 7
        if n % 4 == 3 and a_1 % 4 == 3:
            s = -s
        # 8
        a = n % a_1
        n = a_1
        g *= s


if __name__ == "__main__":
    print(calculate_Jacobi_symbol(20, 313))
