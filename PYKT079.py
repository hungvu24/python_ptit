t = int(input())
for _ in range(t):
    n = int(input())
    a  = [int(x) for x in input().split()]

    cnt = 0
    for i in range(min(a),max(a)):
        if i not in a :
            cnt += 1
    print(cnt)

