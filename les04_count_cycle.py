def numbers(itr, lim):
    mylist = []
    for i in itr:
        if i > lim:
            break
        else:
            mylist.append(i)
    return mylist
