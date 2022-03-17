# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def even_odd():
    numb = input('Введите натуральное число: ')
    even = 0
    odd = 0
    even_n = []
    odd_n = []
    for n in numb:
        x = int(n)
        if x % 2 == 0:
            even_n.append(x)
            even += 1
        else:
            odd_n.append(x)
            odd += 1
    print(f'Четные: {even} {even_n}, нечетные: {odd} {odd_n}')

if __name__ == '__main__':
    even_odd()
