# TASK4 HW3
import random
import string


def create_password(len_pasw):
    arr_pasw = []

# АЛГОРИТМ ПО ПОЛУЧЕНИЮ РАНДОМНЫХ БУКВ, ЦИФР И СПЕЦИАЛЬНЫХ СИМВОЛОВ ИЗ МОДУЛЯ string
# ПОЛУЧЕНИЕ НОВЫХ СИМВОЛОВ БУДЕТ ПРОИСХОДИТ ДО ТЕХ ПОР, КАКУЮ ДЛИНУ ПАРОЛЯ УКАЗАЛ ПОЛЬЗОВАТЕЛЬ
    for i in range(len_pasw):
        if i == 0 or i == 2 or i == 4 or i == 6:
            char = random.choice(string.ascii_letters)
            arr_pasw.append(char)
        elif i == 3 or i == 7:
            char = random.choice(string.punctuation)
            arr_pasw.append(char)
        else:
            char = random.choice(string.digits)
            arr_pasw.append(char)

    password = "".join(arr_pasw)

    return password



def main():

    len_password = int(input("Введите длинну пароля, которую вы хотите получить: "))
    password =  create_password(len_password)

    print("Сгенерированный Пароль: ", password)

if __name__ == '__main__':
    main()

