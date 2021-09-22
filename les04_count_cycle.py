from itertools import count, cycle

def numbers():
    for i in count(3):
        if i > 10:
            break
        else:
            return int(i)
