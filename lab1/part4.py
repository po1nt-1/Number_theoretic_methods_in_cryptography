######################################
#                                    #
#    IV.A. Тест Ферма                #
#    IV.B. Тест Соловэя-Штрассена    #
#                                    #
######################################


import random

from main import Error
from part2 import fast_exponentiation_algorithm_modulo
from part3 import calculating_Jacobi_symbol


def Farm_test(n):
    if not isinstance(n, int):
        raise Error("Некорректные входные данные")

    if n >= 5 and n % 2 != 0:
        # 1
        a = random.randint(2, n-2)
        # 2
        r = fast_exponentiation_algorithm_modulo(a, n - 1, n)
        # 3
        if r == 1:
            return "Число n, вероятно, простое"
        else:
            return "Число n составное"

    raise Error("Некорректные входные данные")


def Soloway_Strassen_test(n):
    if not isinstance(n, int):
        raise Error("Некорректные входные данные")

    if n >= 5 and n % 2 != 0:
        # 1
        a = random.randint(2, n-2)
        # 2
        r = fast_exponentiation_algorithm_modulo(a, (n - 1) // 2, n)
        # 3
        if r != 1 and r != n - 1:
            return "Число n составное"
        # 4
        try:
            s = calculating_Jacobi_symbol(a, n)
        except Error as e:
            raise Error(str(e))
        # 5
        if r % n == s:
            return "Число n, вероятно, простое"
        else:
            return "Число n составное"

    raise Error("Некорректные входные данные")


if __name__ == "__main__":
    f = 23
    print(Farm_test(f))
    print(Soloway_Strassen_test(f))
