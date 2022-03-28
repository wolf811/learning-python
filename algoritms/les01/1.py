# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def sum_mul():
    numb = input('Enter number: ')
    sum = 0
    mul = 1
    for n in numb:
        sum += int(n)
        mul *= int(n)

    print(f'Сумма {numb} = {sum}')
    print(f'Произведение {numb} = {mul}')

if __name__ == '__main__':
    sum_mul()

