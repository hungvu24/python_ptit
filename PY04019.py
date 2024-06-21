class Nhanvien:
    def __init__(self, id , name , score):
        self.id = id
        self.name = name
        self.score = score
    def Ketqua(self):
        if self.score > 9.5:
            return 'XUAT SAC'
        if self.score >= 8:
            return 'DAT'
        if self.score >= 5:
            return 'CAN NHAC'
        return 'TRUOT'

    def __str__(self):
        return '{} {} {:.2f} {}'.format(self.id , self.name , self.score , self.Ketqua())
list = []
for i in range(int(input())):
    id = 'TS0{}'.format(i+1)
    name = input()
    lt = float(input())
    th = float(input())
    lt /= 10 if lt > 10 else 1
    th /= 10 if th > 10 else 1
    list.append(Nhanvien(id , name , (lt + th)/2))
list.sort(key= lambda e : (-e.score))
print(*list,sep='\n')