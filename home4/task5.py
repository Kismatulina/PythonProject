def calculate_danger(depth_mansory):
    return pow(depth_mansory, 3) - 3 * pow(depth_mansory, 2) - 12 * depth_mansory + 10



def find_save_depth(max_danger):

    depth_min = 0
    depth_max = 4


    depth_middle = (depth_min + depth_max) / 2
    m_danger = calculate_danger(depth_middle)

    while abs(m_danger) > max_danger:
        if m_danger > 0:
            depth_min = depth_middle

        else:
            depth_max = depth_middle

        depth_middle = (depth_min + depth_max) / 2
        m_danger = calculate_danger(depth_middle)

    return depth_middle


def main():
    user_max_danger = float(input("Введите допустимый уровень опасности: "))

    if user_max_danger < 0:
        print("Вы ввели некорректное значение попробуйте еще раз")
    else:
        print("Приблизительно безопасная глубина кладки: ", find_save_depth(user_max_danger))



if __name__ == '__main__':
    main()
