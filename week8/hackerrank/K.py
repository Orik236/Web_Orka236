if __name__ == '__main__':
    N = int(raw_input())
    l = []
    for i in range(N):
        a = raw_input().split()
        if a[0] == 'insert':
            a[1], a[2] = int(a[1]), int(a[2])
            t = []
            if len(l) == 0:
                t += [a[2]]
            elif len(l) == 1:
                if a[1] == 0:
                    t += [a[2]] + [l[0]]
                else:
                    t += [l[0]] + [a[2]]
            else:
                t += l[:a[1]] + [a[2]] + l[a[1]:]
            l = t[:]

        elif a[0] == 'print':
            print(l)
        elif a[0] == 'remove':
            a[1] = int(a[1])
            t = []
            ok = True
            for i in l:
                if (i == a[1]) & (ok):
                    ok = False
                else:
                    t += [i]
            l = t[:]
        elif a[0] == 'append':
            a[1] = int(a[1])
            l.append(a[1])
        elif a[0] == 'sort':
            l.sort()
        elif a[0] == 'pop':
            l = l[:len(l)-1]
        else:
            for i in range(len(l)//2):
                l[i], l[len(l)-i-1] = l[len(l)-i-1], l[i]
