fibo = [0 , 1 , 1]
for i in range ( 3 , 93):
    fibo.append(fibo[i-1] + fibo[i-2])
t = int(input())
while t > 0:
    l , r = list(map(int , input().split()))
    for i in range (l , r+1):
        print(fibo[i] , end =' ')
    print()
    t -= 1
