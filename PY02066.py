n = int(input())
a , m , s , ok = [],{},0,0
while len(a) < n:
    x =[int(x) for x in input().split()]
    a += x
for i in a :
    m[i] = 1
    s = max(s,i)
for i in range(1, s + 1):
    if i not in m :
        print(i)
        ok = 1
if ok == 0:
    print("Excellent!")
