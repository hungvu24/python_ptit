def find(a):
    a.sort()
    if a[0] != 1:
        return 1
    for i in range (1 , len(a)):
        if a[i] - a[i-1] > 1:
            return a[i-1]+1
    return a[-1] + 1
n = int(input())
a = list(map(int,input().split()))
print(find(a))