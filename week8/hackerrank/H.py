if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    for i in range(n-1, -1, -1):
        if arr[i] != arr[n-1]:
            print(arr[i])
            break
