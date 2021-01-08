###########################################################
#                                                         #
#    VI. Генерация простого числа заданной размерности    #
#                                                         #
###########################################################


import random

from system import Error
from part5 import Miller_Rabin_test


def generate_prime_number(k, t):
    if not isinstance(k, int) or not isinstance(t, int):
        raise Error("Некорректные входные данные")
    if k < 1 or t < 1:
        raise Error("Некорректные входные данные")

    while True:
        # 1
        p = []
        for _ in range(k):
            p.append(random.randint(0, 1))
        # 2
        p[0], p[-1] = 1, 1
        # 3
        decimal_p = int(''.join(str(i) for i in p), base=2)
        flag = False
        for i in range(2, 201):
            if i == decimal_p:
                break
            if decimal_p % i == 0:
                flag = True
                break
        if flag:
            continue
        # 4
        j = 0
        for i in range(1, t+1):
            j = i
            # 4.1
            # Уже есть в Miller_Rabin_test
            # 4.2
            if Miller_Rabin_test(decimal_p) == "Число n, вероятно, простое":
                continue
            else:
                break

        if j == t:
            return f"Число {decimal_p} простое с вероятностью " +\
                f"{(1 - (1 / (4 ** t))) * 100} %"


if __name__ == "__main__":
    print(generate_prime_number(7, 100))
