n = int(input())
a = [int(x) for x in input().split()]
ok = False
for i in range(1, n):
    if ((a[i]> 0) & (a[i-1] > 0)) | ((a[i] < 0) & (a[i-1] < 0)):
        ok = True
        break

if ok:
    print('YES')
else:
    print('NO')