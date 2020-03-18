x = int(input())
count = 0
for n in range(1, int(x**(1/2))):
    if x % n == 0:
        count+=1
count *= 2
if x % int(x**1/2):
    print(count+1)
else:
    print(count)