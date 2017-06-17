def anti_vowel(text):
    l = []
    vowel = ["A","E","I","O","U"]
    for t in text:
        if t.upper() not in vowel:
            l.append(t)
    return "".join(l)
