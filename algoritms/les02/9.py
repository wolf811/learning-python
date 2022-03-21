# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
def sum_numbers(number):
    sum = 0
    for f in number:
        sum += int(f)
    return sum


def max_number():
    list_number = [i for i in input('Введите несколько чисел через пробел: ').split()]

    max_num = 0
    max_sum = 0
    for i in list_number:
        if sum_numbers(i) > max_sum:
            max_num = i
            max_sum = sum_numbers(i)

    print(f'Число {max_num} наибольшее, его сумма цифр: {max_sum}')
    
if __name__ == '__main__':
    max_number()
