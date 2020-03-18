def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c


def fix_teen(n):
    if (n >= 13) & (n <= 19) & (n != 15) & (n != 16):
        return 0
    else:
        return n
