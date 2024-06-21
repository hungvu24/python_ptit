a,b=  [int(x) for x in  input().split()]
c = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
c.sort()
d.sort()
n ={}
m ={}
for i in c : n[i] = 1
for i in d : m[i] = 1
for i in c :
    if i in d :
        print(i , end=" ")
print()
for i in c :
    if i not in d :
        print(i,end=" ")
print()
for i in d :
    if i not in c :
        print(i , end=" ")