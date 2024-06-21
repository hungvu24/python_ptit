n = int(input())
mang  = [int(i) for i in input().split()]
i = 1
while i < len(mang) :
    if (mang[i -1 ] + mang[i] ) % 2 == 0 :
        mang.pop(i)
        mang.pop(i-1)
        if i > 1 :
            i -= 1
    else :
        i += 1
print(len(mang))
