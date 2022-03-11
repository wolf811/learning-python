# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

def get_alf():
    let1 = input('Введите первую букву: ')
    let2 = input('Введите вторую букву: ')
    pos_let1 = ord(let1) - 64
    pos_let2 = ord(let2) - 64
    # return f'Места букв в алфавите: {let1}, {let2}'
    return f'{let1} - на месте {ord(let1)}; {let2} - на месте {ord(let2)}'
    # alf = {
    #     '1': 'a',
    #     '2': 'b',
    #     '3': 'c',
    # }
    # for k,v in alf.items():
    #     if v == let1:
    #         return k


print(get_alf())
    
