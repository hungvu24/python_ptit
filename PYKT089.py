n = int(input())
a=[]
while len(a) < n:
    a.extend(list(map(int,input().strip().split())))
chan = []
le = []
for i in a :
    if i % 2 == 1:
        le.append(i)
    else: chan.append(i)
chan.sort()
le.sort(reverse= True)
vtl = 0
vtc = 0
for i in a :
    if i % 2 == 1:
        print(le[vtl],end=" ")
        vtl += 1
    else:
        print(chan[vtc] , end=" ")
        vtc += 1