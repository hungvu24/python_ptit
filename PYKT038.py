n = input()
if len(n) % 3 == 2:
    s = "0" + n
elif len(n) % 3 == 1:
    s = "00" + n
else:s = n
s1 =""
tmp = ""
for i in range(len(s)):
    if i % 3 == 2:
        tmp += s[i]
        if tmp == "000": s1+='0'
        elif tmp == "001": s1 += '1'
        elif tmp == "010": s1 += '2'
        elif tmp == "011":
            s1 += '3'
        elif tmp == "100":
            s1 += '4'
        elif tmp == "101":
            s1 += '5'
        elif tmp == "110":
            s1 += '6'
        elif tmp == "111":
            s1 += '7'
        tmp = ""
    else: tmp += s[i]
print(s1)