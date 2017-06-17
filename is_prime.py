def is_prime(X):
    p = 0
    if X < 0:
        p = 2
    else:
        l = []
        y = 0
        o = 0
        m = [0,1]
        for n in range(2,10):
            if X == 0 or X == 1:
                return False
                break
            elif X == 2 or X == 3 or X == 5 or X == 7:
                return True
                break
            elif n > X:
                break
            elif X % n == 0:
                p += 1
            else:
                y = X % n
                l.append(y)
        if p == 1:
            for z in l:
                for n in range(2,10):
                    if z not in m and z % n == 0:
                        p += 1
                        break
                    elif n > z:
                        break
                    else:
                        o = z % n
                        l.append(o)
                        del l[0]           
    if p > 1:
        return False
    else:
        return True
