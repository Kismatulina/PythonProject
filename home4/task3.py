
def main():

    first_num = input("Введите 1-ое число: ")
    second_num = input("Введите 2-ое число: ")
    summa_original_num = int(first_num) + int(second_num)
    print("Сумма цифр: ", summa_original_num)

    reverse_first_num = int(first_num[::-1])
    reverse_second_num = int(second_num[::-1])
    summa_reverse_num = reverse_first_num + reverse_second_num

    print()
    print("1-ое число наоборот: ", reverse_first_num)
    print("2-ое число наоборот: ", reverse_second_num)
    print("Сумма наоборот: ", summa_reverse_num)


if __name__ == '__main__':
    main()