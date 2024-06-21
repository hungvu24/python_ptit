t = int(input())
for _ in range(t):
    s = input()
    d = []
    id = 1
    for i in s :
        if i == '(':
            print(id , end=" ")
            d.append(id)
            id += 1
        elif i == ')':
            print(d[-1],end=" ")
            d.pop()
    print()