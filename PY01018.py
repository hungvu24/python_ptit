p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while 1 :
    nhap = [str(i) for i in input().split()]
    k = int(nhap[0])
    if k == 0 : break
    s = nhap[1]
    res = ""
    for i in s :
        index = p.find(i)
        res += p[(index+k) % 28]
    a = list(res)
    a.reverse()
    for i in a :
        print(i , end = '')
    print()
