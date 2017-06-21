# Last but not least, note that (2 + 3) / 2 is not the same as (2 + 3) / 2.0!
#The former is integer division, meaning Python will try to give you an integer back.
#You'll want a float, so something like (2 + 3) / 2.0 is the way to go.

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
