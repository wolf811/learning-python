# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

def what_letter():
    number = int(input('Введите номер буквы: '))

    let_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    print(let_list)
    if number <= len(let_list):
        print(f'Введенный номер буквы [{number}] - это буква {let_list[number - 1]}')
    else:
        print(f'Введенное число не соответствует количеству букв в алфавите')


if __name__ == '__main__':
    what_letter()
