n = int(input())
a = [int(x) for x in input().split()]
for i in range(n//2):
    a[n-i-1], a[i] = a[i], a[n-i-1]

for i in a:
    print(i, end = ' ')