################################
#                              #
#    V. Тест Миллера-Рабина    #
#                              #
################################


import random

from main import Error
from part2 import fast_exponentiation_algorithm_modulo


def Miller_Rabin_test(n):
    if not isinstance(n, int):
        raise Error("Некорректные входные данные")
    if n < 5 or n % 2 == 0:
        raise Error("Некорректные входные данные")

    # 1
    r = n-1
    s = 0
    while(r % 2 == 0):
        s += 1
        r = int(r / 2)
    # 2
    a = random.randint(2, n-2)
    # 3
    y = fast_exponentiation_algorithm_modulo(a, r, n)
    # 4
    if y != 1 and y != n-1:
        # 4.1
        j = 1
        # 4.2
        while(j <= s-1 and y != n-1):
            # 4.2.1
            y = fast_exponentiation_algorithm_modulo(y, 2, n)
            # 4.2.2
            if y == 1:
                return "Число n составное"
            # 4.2.3
            j += 1
        # 4.3
        if y != n-1:
            return "Число n составное"
    # 5
    return "Число n, вероятно, простое"


if __name__ == "__main__":
    print(Miller_Rabin_test(51))
