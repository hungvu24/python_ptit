class SinhVien:
    def __init__(self, name , year , marks):
        self.name = name
        self.year = year
        self.score = sum(marks)
    def __str__(self):
        return f'{self.name} {self.year} {self.score}'
name = input()
year = input()
marks = [float(input()) , float(input()) , float(input()) ]
print(SinhVien(name , year , marks))