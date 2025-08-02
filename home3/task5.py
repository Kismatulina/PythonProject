# TASK5 HW3

from collections import Counter

def check_anagramm(first_word, second_word):

# ПРОВЕРЯЕМ ДЛИНУ 1-ОГО СЛОВА И ДЛИНУ 2-ГО СЛОВА
# ЕСЛИ ДЛИНА 1-ОГО СЛОВА РАВНА ДЛИНЕ 2-ОГО СЛОВА, ТО ПРОВЕРЯЕМ КОЛИЧЕСТВО ПОВТОРЕНИЙ ЭЛЕМЕНТОВ В КАЖДОМ СЛОВЕ
    if len(first_word) == len(second_word):

        # ПОДСЧИТЫВАЕМ КОЛ-ВО ПОВТОРЕНИЙ ЭЛЕМЕНТОВ С ИСПОЛЬЗОВАНИЕМ МЕТОДА Couter КЛАССА Collections
        # ЕСЛИ КОЛИЧЕСТВО ПОВТОРОВ ЭЛЕМЕНТОВ 1-ОГО СЛОВА РАВНА КОЛ-ВУ ПОВТОРОВ 2-МУ СЛОВА, ТО СЛОВА АНАГРАММЫ
        if Counter(first_word) == Counter(second_word):
            print("Слова {0} и {1} являются анаграммами".format(first_word, second_word))
        else:
            print("Слова {0} и {1} не являются анаграммами".format(first_word, second_word))

    else:
        print("Слова имеют разную длинну, поэтому не являются анаграммами")




def main():
    first_word = input("Введите 1-ое слово: ")
    second_word = input("Введите 2-ое слово: ")

    check_anagramm(first_word, second_word)

if __name__ == '__main__':
    main()
