def median(x):
    if type(x) != list:
        print "Please provide a valid list of numbers"
    else:
        l = sorted(x)
        if len(l) == 1:
            m = l[0]
        elif len(l) % 2 == 0:
            f = abs(len(l) / 2) - 1
            n = abs(len(l) / 2)
            m = (l[f] + l[n])/2.0
        else:
            m = l[abs(len(l) / 2)]
    return m
