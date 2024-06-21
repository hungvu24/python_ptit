t = int(input())
def check(s):
    if len(s) % 2 != 0 or s != s[::-1]:
        return False
    for i in s:
        if int(i) % 2 != 0:
            return False
    return True
while t > 0:
    s = int(input())
    for i in range ( 22 , s , 2):
        if check(str(i)):
            print(i , end=' ')
    print()
    t -= 1

