#######################################
#                                     #
#    IX. Решение системы сравнений    #
#                                     #
#######################################


from system import Error
from part1 import search_for_the_inverse_element_modulo
from part3 import NOD


def solve_congruence_system(n):
    if not isinstance(n, int):
        raise Error("Некорректные входные данные")
    b_list = []
    m_list = []
    for i in range(1, n + 1):
        b = input(f'Введите b{i}: ')
        m = input(f'Введите m{i}: ')
        if b.isnumeric() and m.isnumeric():
            b_list.append(int(b))
            m_list.append(int(m))

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
        Nj = search_for_the_inverse_element_modulo(m_list[i], Mj)
        x = (x + b_list[i] * Mj * Nj) % M

    return x


if __name__ == "__main__":
    print(solve_congruence_system(2))
