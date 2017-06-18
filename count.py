def count(sequence,item):
    c = 0
    l = []
    l = sequence
    if len(l) < 2:
        if l[0] == item:
            c += 1
    else:
        for i in l:
            if type(i) == int:
                if i // 10 == 0:
                    if i == item:
                        c += 1
                else:
                    while i // 10 !=0:
                        if i % 10 == item:
                            c += 1
                            i = i // 10
                        else:
                            i = i // 10
            elif type(i) == list:
                for n in i:
                    if n == item:
                        c += 1
            elif type(i) == str or type(i) == float:
                o = str(i)
                m = o.split()
                for n in m:
                    if n == item:
                        c += 1
    return c
