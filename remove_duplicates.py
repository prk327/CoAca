def remove_duplicates(x):
    l = []
    for n in x:
        if n not in l:
            l.append(n)
    return l
