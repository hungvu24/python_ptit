N = int(input())

# Nhập mảng
A = list(map(int, input().split()))

# Khởi tạo ba số lớn nhất và hai số nhỏ nhất
max1, max2, max3 = float(), float(), float()
min1, min2 = float(), float()

# Tìm ba số lớn nhất và hai số nhỏ nhất trong mảng
for num in A:
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num

    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

# Tính tổng lớn nhất của bộ ba số
max_sum = max(max1 * max2 * max3, min1 * min2 * max1)

# In ra tổng lớn nhất của bộ ba số
print( max_sum)