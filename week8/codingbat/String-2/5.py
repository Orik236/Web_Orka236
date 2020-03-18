def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if len(b) < len(a):
        a, b = b, a
    return b[len(b) - len(a):] == a

