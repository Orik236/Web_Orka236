x = int(input())
i = 0
ok = False
while 2**i <= x:
    if 2**i == x:
        ok = True
    i+=1
if ok:
    print('YES')
else:
    print('NO')