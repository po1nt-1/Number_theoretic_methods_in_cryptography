######################################################
#                                                    #
#    I. Обобщенный (расширенный) алгоритм Евклида    #
#                                                    #
######################################################


def extended_euclidean_algorithm(x, y):
    if x < y and x > 1 and y > 1:
        t = x
        x = y
        y = t
    if x >= y and x > 1 and y > 1:
        # 1
        a1, a2 = 0, 1
        b1, b2 = 1, 0

        # 2
        while y != 0:
            # 2.1
            q = int(x/y)
            r = x - q * y
            a = a2 - q * a1
            b = b2 - q * b1

            # 2.2
            x = y
            y = r
            a2 = a1
            a1 = a
            b2 = b1
            b1 = b

        # 3
        m = x
        a = a2
        b = b2

        # 4
        return m, a, b

    from main import Error
    raise Error("Некорректные входные данные")


def search_for_the_inverse_element_modulo(m, s):
    if not isinstance(m, int) or not isinstance(s, int):
        raise Error("Некорректные входные данные")

    if m > 1:
        # \nss^(-1)≡1(mod m), s^(-1) = ?
        try:
            _, _, b = extended_euclidean_algorithm(m, s)
        except Error as e:
            raise Error(str(e))

        return b  # s^(-1)

    from main import Error
    raise Error("Некорректные входные данные")


if __name__ == "__main__":
    print(extended_euclidean_algorithm(7, 3))
