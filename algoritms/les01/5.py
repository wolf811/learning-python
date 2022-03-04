# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def get_alf():
    let1 = input('Enter first letter: ')
    # let2 = input('Enter second letter: ')
    alf = {
        '1': 'a',
        '2': 'b',
        '3': 'c',
    }
    for k,v in alf.items():
        if v == let1:
            return k


print(get_alf())
    