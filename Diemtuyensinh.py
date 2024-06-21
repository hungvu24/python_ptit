from typing import List

class TuyenSinh:
    def chuanHoa(self, name: str) -> str:
        listName = name.strip().split()
        nameChuanHoa = ""
        for i in listName:
            nameChuanHoa += i.title() + " "
        return nameChuanHoa.strip()

    def tinhTongDiem(self, diemThi: float, khuVuc: str, danToc: str) -> float:
        if khuVuc == "1": diemThi += 1.5
        elif khuVuc == "2": diemThi += 1
        elif khuVuc == "3": diemThi += 0
        if danToc.lower() != "kinh": diemThi += 1.5
        return diemThi

    def status(self, diemThi: float, khuVuc: str, danToc: str) -> str:
        tongDiem = self.tinhTongDiem(diemThi, khuVuc, danToc)
        return "Do" if tongDiem >= 20.5 else "Truot"

    def generaId(self, i: int) -> str:
        ans = str(i)
        while len(ans) < 2:
            ans = "0" + ans
        return "TS" + ans

    def __init__(self, i: int, name: str, diemThi: float, danToc: str, khuVuc: str):
        self.id = self.generaId(i)
        self.name = self.chuanHoa(name)
        self.diemThi = diemThi
        self.danToc = danToc
        self.khuVuc = khuVuc
        self.tongDiem = self.tinhTongDiem(diemThi, khuVuc, danToc)
        self.status = self.status(diemThi, khuVuc, danToc)

    def __str__(self):
        return "{} {} {:.1f} {}".format(self.id, self.name, self.tongDiem, self.status)

t = int(input())
a: List[TuyenSinh] = []
for i in range(t):
    name = input().strip()
    diemThi = float(input().strip())
    danToc = input().strip()
    khuVuc = input().strip()
    ts = TuyenSinh(i + 1, name, diemThi, danToc, khuVuc)
    a.append(ts)

a.sort(key=lambda x: (-x.tongDiem, x.id))
for element in a:
    print(element)