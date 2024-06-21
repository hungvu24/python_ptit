class Bill:
    def __init__(self,id , name , start , end ):
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        self.start = start
        self.end = end
        self.tinhtien()
    def tinhtien(self):
        sokhoi = self.end - self.start
        if sokhoi <= 50:
            self.total = sokhoi * 100
            self.total *= 1.02
        elif sokhoi <= 100:
            self.total = 50*100 + (sokhoi - 50)*150
            self.total *= 1.03
        elif sokhoi <= 200:
            self.total = 50*100 + 50*150 + (sokhoi - 100)*200
            self.total *= 1.05
        self.total = round(self.total)
    def __str__(self):
        return '{} {} {}'.format(self.id , self.name , self.total)
list=[]
for i in range(int(input())):

    name = input()

    end = int(input())
    start = int(input())
    list.append(Bill(i+1 , name , end , start))
list.sort(key=lambda e : (-e.total))
print(*list,sep='\n')
