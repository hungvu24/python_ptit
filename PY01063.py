def check(a , b):
    return a.count(b)
t = int(input())
while t > 0:
    a = input()
    b = input()
    print(check(a , b))
    t -= 1