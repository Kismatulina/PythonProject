# TASK2 HW3

def main():

    user_input = input("Введите числа через ',' : ")

    arr_num = map(int, user_input.split(","))
    max_num = max(arr_num)

    print("В веденном списке - {0}, максимальное число - {1}".format(user_input, max_num))

if __name__ == '__main__':
    main()