a = input()
b = int(input())
m = {}
for i in range(int(len(a)/2)):
    k = int(a[0])*10 + int(a[1])
    if k in m :
        m[k] += 1
    else: m[k] = 1
    a = a[2::]
ok = 0
for i in sorted(m):
    if m[i] >= b:
        ok = 1
        print(i, m[i])
if ok == 0:
    print('NOT FOUND')


