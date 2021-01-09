import inspect
import json
import os
import random
import sys


class Error(Exception):
    pass


def get_script_dir(follow_symlinks=True):
    '''получить директорию со исполняемым скриптом'''
    # https://clck.ru/P8NUA
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


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
                if (a * r - b) % m == 0:
                    N.append(r)
            for i in N:
                for j in range(k):
                    pass
            break
    return f"x ≡ {i + j * m} (mod {L})"


def zap(ans):
    rez = open('rezult', 'w')
    rez.write(ans)
    rez.close


def func(a, b, c, p):
    if c >= (p // 2):
        c1 = (b * c) % p
    if c < (p // 2):
        c1 = (a * c) % p
    return c1


def Farm_test(n):
    if not isinstance(n, int):
        raise Error("Некорректные входные данные")

    if n >= 5 and n % 2 != 0:
        # 1
        a = random.randint(2, n-2)
        # 2
        r = pow(a, n - 1, n)
        # 3
        if r == 1:
            return "Число n, вероятно, простое"
        else:
            return "Число n составное"

    raise Error("Некорректные входные данные")


def main():
    try:
        path_ = os.path.join(get_script_dir(), 'in.json')
        if not os.path.exists(path_):
            with open(path_, "w", encoding='utf-8') as f:
                json.dump({"p": 1, "a": 1, "b": 1}, f)

        with open(path_, "r", encoding='utf-8') as f:
            data = json.load(f)

        p = int(data["p"])
        a = int(data["a"])
        b = int(data["b"])

        if b <= 1 or b >= p:
            raise Error("Некорректные входные данные")
        if Farm_test(p) == "Число n составное":
            raise Error("Некорректные входные данные")
        r = 0
        for i in range(1, 100):
            if (a ** i) % p == 1:
                r = i
                break
        # 1
        u = 2
        v = 2
        c = ((a ** u) * (b ** v)) % p
        d = c
        # 2
        kc = 2
        kd = 2
        xc = 2
        xd = 2
        while True:
            if c >= (p // 2):
                xc = xc + 1
            else:
                kc = kc + 1
            if d >= (p // 2):
                xd = xd + 1
            else:
                kd = kd + 1
            c = func(a, b, c, p)
            d = func(a, b, d, p)
            d = func(a, b, d, p)
            if c == d:
                break
        # 3
        xcd = xc - xd
        kcd = kd - kc
        x = solve_linear_congruence(xcd, kcd, r)

        with open(os.path.join(get_script_dir(), 'out.json'), "w",
                  encoding='utf-8') as f:
            f.write(x)
    except KeyboardInterrupt as e:
        print(e)


if __name__ == "__main__":
    main()
