def reverse(text):
    l = []
    for t in range(len(text)-1,-1,-1):
        l.append(text[t])
    return "".join(l)
