# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def get_alf():
    let1, let2 = [
        i.upper() for i in input('Введите две латинские буквы через пробел: ').split()
    ]

    let_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    index_let1 = let_list.index(let1) + 1
    index_let2 = let_list.index(let2) + 1

    if index_let1 < index_let2:
        step = 1
    else:
        step = -1

    print(f'Буква {let1} на позиции: {index_let1}')
    print(f'Буква {let2} на позиции: {index_let2}')

    print(
        f'Между ними буквы: \
    {let_list[let_list.index(let1) + step:let_list.index(let2):step]} \
    ({abs(index_let1 - index_let2) - 1})'
    )


if __name__ == '__main__':
    get_alf()

    
