s = input()
upper = 0
for i in range(0 , len(s)) :
    if s[i].isupper():
        upper += 1
lower = len(s) - upper
if (lower < upper) :
    print(s.upper())
else :
    print(s.lower())
