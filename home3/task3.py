# TASK3 HW3

# 1-ый способ проверки полиндрома (использование срезов)
# def check_palin(word):
#     reverse_word = word[::-1]
#     if word == reverse_word:
#         print("Слово - {0} является палиндромом".format(word))
#     else:
#         print("Слово - {0} не является палиндромом".format(word))
#
# def main():
#     user_word = input("Введите слово, которое хотите проверить на палиндром: ").lower()
#     check_palin(user_word)
#
# if __name__ == '__main__':
#     main()




# 2-ой способ(использование встроенного метода reversed)
def check_palin(word):
    reverse_word = "".join(reversed(word))
    if word == reverse_word:
        print("Слово - {0} является палиндромом".format(word))
    else:
        print("Слово - {0} не является палиндромом".format(word))


def main():
    user_word = input("Введите слово, которое хотите проверить на палиндром: ").lower()
    check_palin(user_word)


if __name__ == '__main__':
        main()