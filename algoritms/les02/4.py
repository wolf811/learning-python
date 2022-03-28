# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
def sum_elem():
    n = int(input('Введите количество элементов: '))
    i = 0
    range_num = 1
    sum = 0
    while i < n:
        sum += range_num
        range_num /= -2
        i += 1

    print(f'Сумма {sum}')


if __name__ == '__main__':
    sum_elem()
