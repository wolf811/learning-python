# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

def sum_mul():
    n = int(input('Enter number: '))
    sum = 0
    mul = 1

    while n > 0:
        numb = n % 10
        sum += numb
        mul *= numb
        n = n // 10

    print("Сумма:", sum)
    print("Произведение:", mul)

if __name__ == '__main__':
    sum_mul()
