######################################
#                                    #
#    IV.A. Тест Ферма                #
#    IV.B. Тест Соловэя-Штрассена    #
#                                    #
######################################


import random

from system import Error
from part2 import fast_exponentiation_algorithm_modulo


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


def Jacobi(n, a):
    if n < 3 or n % 2 == 0 or a < 0 or a >= n:
        raise Error("Некорректные входные данные")

    g = 1
    j = None
    m = 0
    while j is None:
        if a == 0:
            j = 0
            break
        if a == 1:
            j = g
            break
        for k in range(1, a):
            if (a % (2**k)) == 0 and ((a/(2**k)) % 2) != 0:
                c = int(a/(2**k))
                m = k
                break
            else:
                m = 0
                c = a
        if (m % 2) != 0 and ((n % 8) == 3 or (n % 8) == 5):
            s = -1
        else:
            s = 1
        if (n % 4) == 3 and (c % 4) == 3:
            s = -s
        if c == 1:
            j = g*s
        a = n % c
        n = c
        g = g*s

    return j


def Soloway_Strassen_test(n):
    if n < 5 or n % 2 == 0:
        raise Error("Некорректные входные данные")
    a = random.randint(2, n - 2)
    b = int((n - 1) / 2)
    c = int(a ** b)
    r = int(c % n)
    j = None
    while True:
        if r != 1 and r != n-1:
            return 'Число составное'
        else:
            j = Jacobi(n, a)
        if (r % n) == j:
            return 'Число, вероятно, простое'
        else:
            return 'Число составное'


if __name__ == "__main__":
    numbers = 500
    iterations = 10000

    with open('/home/po1nt/code/Number_theoretic_methods_in_cryptography/lab1/out.txt', 'w', encoding='utf-8') as f:
        for value in range(5, numbers, 2):
            results = []
            flag = False
            for i in range(iterations):
                try:
                    results.append(Soloway_Strassen_test(value))
                except Error:
                    flag = True
            if flag:
                continue

            primes = 0
            not_primes = 0
            for elem in results:
                if elem == 'Число составное':
                    not_primes += 1
                elif elem == 'Число, вероятно, простое':
                    primes += 1

            f.write(f'Число:\t{value}\t')
            print(f'Число:\t{value}', end='\t')
            if primes > not_primes:
                f.write(
                    f"Простое: {round((primes / iterations) * 100, 4)}%\n")
                print(
                    f"\033[33m Простое: {round((primes / iterations) * 100, 4)}%\033[0m")

            elif not_primes >= primes:
                f.write(
                    f'Составное: {round((not_primes / iterations) * 100, 4)}%\n')
                print(
                    f'Составное: {round((not_primes / iterations) * 100, 4)}%')
