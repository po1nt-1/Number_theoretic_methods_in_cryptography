#######################################
#                                     #
#    IX. Решение системы сравнений    #
#                                     #
#######################################


from system import Error


def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modinv(a, b):
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Error("Некорректные входные данные")
    return x % b


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def solve_congruence_system(n, b_list=[], m_list=[]):
    if not isinstance(n, int):
        raise Error("Некорректные входные данные")

    max_m = max(m_list)
    for mi in m_list:
        for mj in m_list:
            try:
                nod = NOD(mi, mj)
            except Error:
                continue
            if mi != mj and nod != 1:
                raise Error("Некорректные входные данные")

    M = 1
    for m in m_list:
        M *= m

    x = 0
    for i in range(n):
        Mj = M // m_list[i]
        Nj = modinv(Mj, m_list[i])
        x = (x + b_list[i] * Mj * Nj) % M

    return x


if __name__ == "__main__":
    maximum = 20

    with open('/home/po1nt/code/Number_theoretic_methods_in_cryptography/lab1/out.txt', 'w', encoding='utf-8') as f:
        for i in range(1, maximum):
            for j in range(1, maximum):
                for p in range(1, maximum):
                    for q in range(1, maximum):

                        for ii in range(1, maximum):
                            for jj in range(1, maximum):
                                print(f'b1={i}', f'm1={j}', f'b2={p}',
                                      f'm2={q}', f'b3={ii}', f'm3={jj}', end='')
                                f.write(
                                    f'b1={i} m1={j} b2={p} m2={q} b3={ii} m3={jj}')

                                try:
                                    x = solve_congruence_system(
                                        3, b_list=[i, p, ii], m_list=[j, q, jj])

                                    print('\t\tx =', x, f'mod( {j * q * jj} )')
                                    f.write(
                                        f'\t\tx = {x} mod ( {j * q * jj} )\n')
                                except Error as e:
                                    print(f'\t\t{e}')
                                    f.write(f'\t\t{e}\n')
                                finally:
                                    print()
