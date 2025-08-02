import random


def rock_paper_scissors():
    date_for_computer = ['камень', 'ножницы', 'бумага']
    print(random.choice(date_for_computer))

    # ПОСМОТРЕТЬ РАБОТУ ОТРАБОТКИ ВЫБОРА МЕЖДУ ПОЛЬЗОВАТЕЛЕМ И КОМПЬЮТЕРОМ

    while True:
        print('''\n ДОБРО ПОЖАЛОВАТЬ В ИГРУ "КАМЕНЬ, НОЖНИЦЫ, БУМАГА"

                1: Играем!
                0: Выйти

        ''')

        user_choose = input("Введите выбор: ")

        if user_choose == '1':

            user = input("Введите - 'камень', 'ножницы' или 'бумага' : ").lower()

            computer_choose = random.choice(date_for_computer)

            if user_choose == 'камень' and computer_choose == 'ножницы':
                print("\nПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose,
                                                                                                     computer_choose))
            elif user_choose == 'камень' and computer_choose == 'бумага':
                print("\nВЫ ПРОИГРАЛИ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose, computer_choose))
            elif user_choose == 'камень' and computer_choose == 'камень':
                print("\nНИЧЬЯ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose, computer_choose))
            elif user_choose == 'ножницы' and computer_choose == 'камень':
                print("\nВЫ ПРОИГРАЛИ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose, computer_choose))
            elif user_choose == 'ножницы' and computer_choose == 'ножницы':
                print("\nНИЧЬЯ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose, computer_choose))
            elif user_choose == 'ножницы' and computer_choose == 'бумага':
                print("\nПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose,
                                                                                                     computer_choose))
            elif user_choose == 'бумага' and computer_choose == 'камень':
                print("\nПОЗДРАВЛЯЕМ, ВЫ ПОБЕДИЛИ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose,
                                                                                                     computer_choose))
            elif user_choose == 'бумага' and computer_choose == 'ножницы':
                print("\nВЫ ПРОИГРАЛИ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose, computer_choose))
            elif user_choose == 'бумага' and computer_choose == 'бумага':
                print("\nНИЧЬЯ! \nВаш выбор - {0}, выбор компьютера - {1}".format(user_choose, computer_choose))

        elif user_choose == '0':
            break


def guess_the_number():
    random_num = random.randint(1, 100)
    print("\nДОБРО ПОЖАЛОВАТЬ В ИГРУ 'УГАДАЙ ЧИСЛО'")

    while True:
        user_num = int(input("Введите загаданное число: "))

        if user_num < random_num:
            print("\nЧисло больше")
        elif user_num > random_num:
            print("\nЧисло меньше")
        else:
            print("\nВы УГАДАЛИ! \n ВАШЕ ЧИСЛО - {0}, ЗАГАДАННОЕ ЧИСЛО - {1}".format(user_num, random_num))
            break


def mainMenu():
    while True:
        print('''
                1: Игра "Камень, ножницы, бумага"
                2: Игра "Угадай число"
                0: Выйти

                ''')

        user_choose = input("Введите выбор: ")

        if user_choose == '1':
            rock_paper_scissors()
        elif user_choose == '2':
            guess_the_number()
        elif user_choose == '0':
            break


if __name__ == '__main__':
    mainMenu()