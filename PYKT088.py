def Solve (num):
    cnt = 0
    i = 1
    while i*i <= num:
        if num % i == 0:
            if i*i == num:
                cnt += 1
            else:
                cnt += 2
        i+=1
    return cnt == 9
def check(n):
    cnt = 0
    for num in range(1 , n+1):
        if Solve(num):
            cnt += 1
    return cnt
n = input()
print(check(int(n)))