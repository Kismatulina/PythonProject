
def maximum_of_two(num1, num2):
    return max(num1, num2)


def maximum_of_three(num1, num2, num3):
    return max(num1, num2, num3)



def main():
    num1 = int(input("Введите 1-ое число: "))
    num2 = int(input("Введите 2-ое число: "))
    num3 = int(input("Введите 3-е число: "))

    print("Максимальное число между {0} и {1} - {2}".format(num1, num2, maximum_of_two(num1, num2)))
    print("Максимальное число между {0} {1} и {2} - {3}".format(num1, num2, num3, maximum_of_three(num1, num2, num3)))

if __name__ == '__main__':
    main()