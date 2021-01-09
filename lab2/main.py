import inspect
import json
import os
import random
import sys
from math import log


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


def func(x, n):
    return ((x ** 2) + 1) % n


def euclidean_algorithm(x, y):
    if x >= y:
        while y != 0:
            r = x % y
            x = y
            y = r
        return x
    else:
        while x != 0:
            r = y % x
            y = x
            x = r
        return y


def pollard_1(n, c):
    # 1
    a = c
    b = c
    while True:
        # 2
        a = func(a, n)
        b = func(func(b, n), n)
        # 3
        d = euclidean_algorithm(a - b, n)
        # 4
        if 1 < d and d < n:
            p = d
        if d == n:
            return 'Делитель не найден'
        elif d == 1:
            continue


def pollard_2(n):
    # 1
    B = []
    with open(os.path.join(get_script_dir(), 'base.json'), 'r',
              encoding='utf-8') as f:
        B = json.load(f)
    # 2
    a = random.randint(2, n - 2)
    d = euclidean_algorithm(a, n)
    if d >= 2:
        p = d
        return p
    # 3
    for i, p_i in enumerate(B):
        # 3.1
        L = (log(n)) // log(p_i)
        # 3.2
        a = (a ** (p_i ** L)) % n
    # 4
    d = euclidean_algorithm(a - 1, n)
    # 5
    if d == 1 or d == n:
        return 'Делитель не найден'
    else:
        p = d
        return p


if __name__ == "__main__":
    while True:
        print("Выберите алгоритм:")
        print("1)\tρ-метод Полларда;")
        print("2)\t(ρ-1)-метод Полларда;")
        print("0)\tВыход.\n")

        try:
            exit = False
            choice = input("Выбор: ")
            if choice == '0':
                exit = True
                break
            elif choice == '1':
                print(pollard_1(
                    int(input('n=')), int(input('c='))
                ))
            elif choice == '2':
                print(pollard_2(
                    int(input('n='))
                ))
            else:
                print("\tНекорректный ввод.")
        except ValueError:
            print("\tНекорректные входные данные.")
        except Error as e:
            print(f'\t{e}.')
        finally:
            if exit:
                break
            print("\nВыберите действие: ")
            print("1)\tВернуться в меню;")
            print("0)\tВыход.\n")
            choice = input("Выбор: ")
            if choice == '1':
                continue
            elif choice == '0':
                break
