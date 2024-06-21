t = int(input())
def Somayman(n) :
    for i in n :
        if i != '4' and i != '7' :
            return 'NO'
    return 'YES'
while t > 0 :
    n = input()
    print(Somayman(n))
    t -= 1
