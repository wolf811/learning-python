# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def multiples():
    list_one = [i for i in range(2, 100)]
    list_two = [x for x in range(2, 10)]
    res = {}
    for t in list_two:
        res[t] = []
        for o in list_one:
            if o % t == 0:
                res[t].append(o)
        print(f'Для {t} кратны - {len(res[t])}. Кратные числа: {res[t]}')
        
if __name__=='__main__':
    multiples()
