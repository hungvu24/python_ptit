import sys
intMaxValue = sys.maxsize
intMinValue = -sys.maxsize - 1
def check(s : str) -> bool:
	sum = 0
	for i in s :
		if not i.isdigit():
			return True
		sum = sum * 10 + int(i)
	if intMinValue <= sum and sum <= intMaxValue :
		return False
	return True
a = []
with open("DATA.in" , mode="r") as file:
    for element in file.readlines():
        for value in element.split():
            if check(value): a.append(value)
for i in sorted(a):
    print(i , end = " ")
