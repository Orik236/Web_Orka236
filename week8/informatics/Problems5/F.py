n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for i in range(1, n-1):
    if (a[i] > a[i+1]) & (a[i] > a[i-1]):
        cnt+=1
print(cnt)