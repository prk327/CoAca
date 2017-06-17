def censor(text,word):
    l = []
    l = text.split(" ")
    m = []
    for w in l:
        if w.lower() in word.lower():
            m.append("*" * len(word))
        else:
            m.append(w)
    return " ".join(m)
