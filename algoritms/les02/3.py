# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

def flip_number():
    numb = input('Введите число: ')
    numb_list = list(numb)
    numb_list.reverse()
    bmun = ''.join(numb_list)
    print(bmun)


if __name__ == '__main__':
    flip_number()
