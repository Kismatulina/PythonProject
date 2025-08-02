def summa(first_num, second_num):
    return first_num + second_num


def differrence(first_num, second_num):
    return first_num - second_num


def max_num(first_num, second_num):
    return max(first_num, second_num)


def min_num(first_num, second_num):
    return min(first_num, second_num)


def main():
    user_num1 = int(input("Введите 1-ое число: "))
    if user_num1 < 0:
        print("Вы ввели отрицательное 1-ое число")

    else:
        user_num2 = int(input("Введите 2-ое число: "))

        if user_num2 < 0:
            print("Вы ввели отрицательное 2-ое число")

        else:

            while True:
                print('''\nКакую операцию хотите сделать?

                        1: Сложить
                        2: Вычесть
                        3: Максимальное число
                        4: Минимальное число
                        0: Выйти
                    ''')

                user_input = input("Ваш выбор: ")

                if user_input == '1':
                    print("Сумма чисел = ", summa(user_num1, user_num2))
                elif user_input == '2':
                    print("Разность чисел = ", differrence(user_num1, user_num2))
                elif user_input == '3':
                    print("Максимальное число: ", max_num(user_num1, user_num2))
                elif user_input == '4':
                    print("Минимальное число: ", min_num(user_num1, user_num2))
                elif user_input == '0':
                    break
                else:
                    print("Вы ввели не существующую команду, попроюуйте еще раз")


if __name__ == '__main__':
    main()