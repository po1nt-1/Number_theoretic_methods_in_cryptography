import inspect
import os
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


def choice_1():
    a = input("Value1: ")
    b = input("Value2: ")

    print([a, b])


def choice_2():
    path = os.path.join(get_script_dir(), 'input.txt')
    if not os.path.exists(path):
        raise Error("input.txt не найден")

    data = []
    with open(path, 'r', encoding="utf-8") as file:
        for line in file:
            if not line.isspace():
                if '\n' in line:
                    line = line.split('\n')[0]
                data.append(line)

    return data


def select_input_type():
    while True:
        print("Выберите метод ввода данных:")
        print("1 - ручной способ")
        print("2 - чтение из '<script_dir>/input.txt'")
        print()
        print("0 - вернуться назад")

        choice = input("Choice: ")
        if choice == '1':
            choice_1()
        elif choice == '2':
            choice_2()
        elif choice == '0':
            break
        else:
            print("Некорректный ввод")
            continue


def main():
    select_input_type()


if __name__ == "__main__":
    main()
