################################################
#                                              #
#    VIII. Решение сравнения второй степени    #
#                                              #
################################################


from system import Error
from part3 import calculate_Jacobi_symbol
from part5 import Miller_Rabin_test


def solve_quadratic_congruence(p, a, N):
    if not isinstance(a, int) or not isinstance(N, int) or \
            not isinstance(p, int):
        raise Error("Некорректные входные данные")
    if p == 2 or a % p == 0:
        raise Error("Некорректные входные данные")
    if p != 3:
        if Miller_Rabin_test(p) == "Число n составное":
            raise Error("Некорректные входные данные")
    if calculate_Jacobi_symbol(a, p) != -calculate_Jacobi_symbol(N, p) or \
            calculate_Jacobi_symbol(a, p) != 1 or \
            -calculate_Jacobi_symbol(N, p) != 1:
        raise Error("Некорректные входные данные")
    # 1
    n = p
    i = 2
    Pr = []
    while i*i <= n:
        while n % i == 0:
            Pr.append(i)
            n = n/i
        i = i + 1
    if n > 1:
        Pr.append(n)
    if p != Pr[0]:
        raise Error("Некорректные входные данные")
    for L in range(0, p):
        if ((p - 1) % (2 ** L)) == 0 and (((p - 1) / (2 ** L)) % 2) != 0:
            h = int((p - 1) / (2 ** L))
            k = L
    # 2
    a1 = int(pow(a, (h + 1) // 2, p))
    a2 = (1 / a) % p
    N1 = pow(N, h, p)
    N2 = 1
    j = 0
    # 3
    result = []
    for i in range(0, k):
        # 3.1
        b = (a1 * N2) % p
        # 3.2
        c = (a2 * (b ** 2)) % p
        # 3.3
        power = 2 ** (k - 2 - i)
        d = c ** power % p
        if d == 1:
            j = 0
        if d == -1:
            j = 1
        # 3.4
        N2 = (N2 * (N1 ** ((2 ** i) * j))) % p
        x = f'x ≡ {(a1 * N2) % p} (mod {p})'
        if x not in result:
            result.append(x)
            result.append(x.replace('≡', '≡ -'))

    return result


if __name__ == "__main__":
    print(solve_quadratic_congruence(31, 14, 6))
