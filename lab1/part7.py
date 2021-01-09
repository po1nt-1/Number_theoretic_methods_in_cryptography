###############################################
#                                             #
#    VII. Решение сравнения первой степени    #
#                                             #
###############################################


from part3 import NOD


def solve_linear_congruence(a, b, m):
    # 1
    d = NOD(a, m)
    if b % d != 0:
        return "Решений нет"
    k = d
    L = m
    while b % d == 0:
        #  2
        if d != 1:
            a //= d
            b //= d
            m //= d
            d = NOD(a, m)
        else:
            N = []
            for r in range(L):
                if (a*r - b) % m == 0:
                    N.append(r)
            for i in N:
                for j in range(k):
                    pass
            break
    return f"x ≡ {i + j * m} (mod {L})"


if __name__ == "__main__":
    print(solve_linear_congruence(7, 2, 2531))
