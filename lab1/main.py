import os

import part1
import part2
import part3
import part4
import part5
import part6
import part7
import part8
import part9
from system import Error, get_script_dir


def main():
    while True:
        print("Выберите алгоритм:")
        print("1)\tОбобщенный (расширенный) алгоритм Евклида;")
        print("2)\tАлгоритм быстрого возведения в степень;")
        print("3)\tАлгоритм быстрого возведения в степень по модулю;")
        print("4)\tВычисление символа Якоби;")
        print("5)\tТест Ферма;")
        print("6)\tТест Соловэя-Штрассена;")
        print("7)\tТест Миллера-Рабина;")
        print("8)\tГенерация простого числа заданной размерности;")
        print("9)\tРешение сравнения первой степени;")
        print("10)\tРешение сравнения второй степени;")
        print("11)\tРешение системы сравнений;")
        print("0)\tВыход.\n")

        try:
            exit = False
            choice = input("Выбор: ")
            if choice == '0':
                exit = True
                break
            elif choice == '1':
                print(part1.extended_euclidean_algorithm(
                    int(input('x=')), int(input('y='))
                ))
            elif choice == '2':
                print(part2.fast_exponentiation_algorithm(
                    int(input('a=')), int(input('n='))
                ))
            elif choice == '3':
                print(part2.fast_exponentiation_algorithm_modulo(
                    int(input('a=')), int(input('s=')), int(input('m='))
                ))
            elif choice == '4':
                print(part3.calculate_Jacobi_symbol(
                    int(input('a=')), int(input('n='))
                ))
            elif choice == '5':
                print(part4.Farm_test(
                    int(input('n='))
                ))
            elif choice == '6':
                print(part4.Soloway_Strassen_test(
                    int(input('n='))
                ))
            elif choice == '7':
                print(part5.Miller_Rabin_test(
                    int(input('n='))
                ))
            elif choice == '8':
                print(part6.generate_prime_number(
                    int(input('k=')), int(input('t='))
                ))
            elif choice == '9':
                print(part7.solve_linear_congruence(
                    int(input('a=')), int(input('b=')), int(input('m='))
                ))
            elif choice == '10':
                print(part8.solve_quadratic_congruence(
                    int(input('p=')), int(input('a=')), int(input('N='))
                ))
            elif choice == '11':
                print(part9.solve_congruence_system(
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


if __name__ == "__main__":
    main()
