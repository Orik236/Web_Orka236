n = int(input())
a = [int(x) for x in input().split()]
for i in range(0, n, 2):
    print(a[i], end = ' ')