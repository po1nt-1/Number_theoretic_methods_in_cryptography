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


def fast_exponentiation_algorithm_modulo(a, s, n):
    # 1
    nn = bin(s).split('b')[1][::-1]
    y = a
    b_0 = int(nn[0])
    x = a ** b_0
    # 2
    for i, b_i in enumerate(nn):
        if i == 0:
            continue
        y = (y ** 2) % n
        # 2.1
        if int(b_i) == 1:
            x = (x * y) % n
    # 3
    return x


def fast_exponentiation_algorithm_modulo(a, s, n):
    # 1
    nn = bin(s).split('b')[1][::-1]
    y = a
    b_0 = int(nn[0])
    x = a ** b_0

    # 2
    for i, b_i in enumerate(nn):
        if i == 0:
            continue

        y = (y ** 2) % n

        # 2.1
        if int(b_i) == 1:
            x = (x * y) % n

    # 3
    return x


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
            return decimal_p


def extended_euclidean_algorithm(x, y):
    if x < y and x > 1 and y > 1:
        t = x
        x = y
        y = t
    if x >= y and x > 1 and y > 1:
        # 1
        a1, a2 = 0, 1
        b1, b2 = 1, 0

        # 2
        while y != 0:
            # 2.1
            q = x // y
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


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def e_options(PHI):
    primes = []
    with open(os.path.join(get_script_dir(), 'primes.json'), 'r',
              encoding='utf-8') as f:
        primes = json.load(f)

    my_len = len(primes)
    while (2 in primes or 0 in primes):
        my_len = len(primes)
        for i in range(my_len):
            if primes[i] == 2 or primes[i] == 0:
                del primes[i]
                my_len -= 1
                break

    my_len = len(primes)
    while (True):
        nod_false = True
        my_len = len(primes)
        for i in range(my_len):
            if NOD(PHI, primes[i]) != 1:
                del primes[i]
                my_len -= 1
                nod_false = False
                break
        if nod_false is False:
            continue
        else:
            break
    return primes


def gen_key_pair(k):
    t = 30
    p = generate_prime_number(k, t)
    q = generate_prime_number(k, t)
    n = p * q
    while (p == q):
        q = generate_prime_number(k, t)
    PHI = (p - 1) * (q - 1)
    e_primes = e_options(PHI)
    print("Значения для параметра e: ", e_primes[0:10])
    while (True):
        try:
            e = int(input("Введите e: "))
        except ValueError:
            print("Ошибка при вводе 'e'!")
            continue
        if e not in e_primes:
            print("Ошибка при вводе 'e'!")
            continue
        break
    publicExponent = e
    N = n
    public_key = [publicExponent, N]
    res = extended_euclidean_algorithm(PHI, e)
    d = res[2]
    if d < 0:
        d += PHI
    privateExponent = d
    prime1 = p
    prime2 = q
    exponent1 = d % (p - 1)
    exponent2 = d % (q - 1)
    coefficient = (q - 1) % p
    private_key = [privateExponent, prime1, prime2, exponent1,
                   exponent2, coefficient]

    with open(os.path.join(get_script_dir(), 'public_key.json'), 'w',
              encoding='utf-8') as f:
        json.dump(public_key, f)
    print("Открытый ключ сохранен!")
    with open(os.path.join(get_script_dir(), 'private_key.json'), 'w',
              encoding='utf-8') as f:
        json.dump(private_key, f)
    print("Закрытый ключ сохранен!")
    return [public_key, private_key]


def encryption(plain_text, public_key=None):
    plain_char_list = []
    for char in plain_text:
        plain_char_list.append(ord(char))

    if public_key is None:
        try:
            with open(os.path.join(get_script_dir(), 'public_key.json'), 'r',
                      encoding='utf-8') as f:
                public_key = json.load(f)
        except json.decoder.JSONDecodeError as e:
            raise Error("Некорректные входные данные")

    cipher_char_list = []
    for i, char in enumerate(plain_char_list):
        temp = fast_exponentiation_algorithm_modulo(
            char, public_key[0], public_key[1])
        cipher_char_list.append(temp)
    print("Зашифрованное сообщение: ", cipher_char_list)
    return cipher_char_list


def decryption(cipher_char_list, private_key=None, public_key=None):
    plain_char_list = []
    for i, cipher_char in enumerate(cipher_char_list):
        temp = fast_exponentiation_algorithm_modulo(
            cipher_char, private_key[0], public_key[1])
        plain_char_list.append(temp)

    if public_key is None:
        try:
            with open(os.path.join(get_script_dir(), 'public_key.json'), 'r',
                      encoding='utf-8') as f:
                public_key = json.load(f)
        except json.decoder.JSONDecodeError as e:
            raise Error("Некорректные входные данные")

    if private_key is None:
        try:
            with open(os.path.join(get_script_dir(), 'private_key.json'), 'r',
                      encoding='utf-8') as f:
                private_key = json.load(f)
        except json.decoder.JSONDecodeError as e:
            raise Error("Некорректные входные данные")

    plain_text = ''
    for i in range(len(plain_char_list)):
        temp = chr(plain_char_list[i])
        plain_text = plain_text + temp
    print("Расшифрованное сообщение: ", plain_text)
    return plain_text


def main():
    try:
        public_key, private_key = gen_key_pair(16)

        cipher_char_list = encryption(
            plain_text=input("Введите сообщение: "), public_key=public_key)

        plain_text = decryption(
            cipher_char_list, private_key=private_key, public_key=public_key)
    except Error as e:
        print(e)


if __name__ == "__main__":
    main()
