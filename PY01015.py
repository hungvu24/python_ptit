t = int(input())
def so_khong_giam(n):
    for i in range(0,len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True
while t > 0 :
    n = input()
    if so_khong_giam(n):
        print('YES\n')
    else :
        print('NO\n')
