######################################################
#                                                    #
#    I. Обобщенный (расширенный) алгоритм Евклида    #
#                                                    #
######################################################


class Error(Exception):
    pass


def extended_euclidean_algorithm(x, y):
    x = str(x)
    y = str(y)

    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)

        if x >= y and x > 1 and y > 1:
            # 1
            a1, a2 = 0, 1
            b1, b2 = 1, 0

            # 2
            while y != 0:
                # 2.1
                q = round(x/y)
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

    raise Error("Некорректные входные данные")


def main(m, s):
    m = str(m)

    if m.isdigit():
        m = int(m)

        if m > 1:
            print("\nss^(-1)≡1(mod m), s^(-1) = ?\n")
            _, _, b = extended_euclidean_algorithm(m, s)

            print("s^(-1) =", b)

            return b

    raise Error("Некорректные входные данные")


if __name__ == "__main__":
    main(3, 2)
