t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int , input().split()))
    a.sort(reverse=True)
    max_sum=sum(a[:3])
    print(max_sum)