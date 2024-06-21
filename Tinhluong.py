class phongban:
    def __init__(p, ma, ten):
        p.ma = ma
        p.ten = ten

    def __str__(p):
        return p.ten


class nhanvien:
    def __init__(nv, ma, ten, lcb, nc, phong):
        nv.ma = ma
        nv.ten = ten
        nv.luong = lcb * nc * 1000
        nv.phong = phong
        nv.tinhtoan()

    def tinhtoan(nv):
        a = int(nv.ma[1:3])
        if nv.ma[0] == "A":
            if a >= 1 and a <= 3:
                nv.luong *= 10
            elif a >= 4 and a <= 8:
                nv.luong *= 12
            elif a >= 9 and a <= 15:
                nv.luong *= 14
            elif a >= 16:
                nv.luong *= 20
        elif nv.ma[0] == "B":
            if a >= 1 and a <= 3:
                nv.luong *= 10
            elif a >= 4 and a <= 8:
                nv.luong *= 11
            elif a >= 9 and a <= 15:
                nv.luong *= 13
            elif a >= 16:
                nv.luong *= 16
        elif nv.ma[0] == "C":
            if a >= 1 and a <= 3:
                nv.luong *= 9
            elif a >= 4 and a <= 8:
                nv.luong *= 10
            elif a >= 9 and a <= 15:
                nv.luong *= 12
            elif a >= 16:
                nv.luong *= 14
        elif nv.ma[0] == "D":
            if a >= 1 and a <= 3:
                nv.luong *= 8
            elif a >= 4 and a <= 8:
                nv.luong *= 9
            elif a >= 9 and a <= 15:
                nv.luong *= 11
            elif a >= 16:
                nv.luong *= 13

    def __str__(nv):
        return "{} {} {} {}".format(nv.ma, nv.ten, nv.phong, nv.luong)


p = []
for i in range(int(input())):
    s = [i for i in input().split()]
    ten = ''
    for i in range(1, len(s)):
        ten += s[i] + " "
    p.append(phongban(s[0], ten))
nv = []
for i in range(0, int(input())):
    s = input()
    for j in p:
        if j.ma == s[3:]:
            nv.append(nhanvien(s, input(), int(input()), int(input()), j))
print(*nv, sep="\n")