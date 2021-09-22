from itertools import count

for el in count(7):
    if el > 15:
        break
    else:
        print(el)
