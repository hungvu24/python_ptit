def process_sequence(arr, m):
    max_value = max(arr)

    max_index = arr.index(max_value)
    arr.insert(max_index, m)

    arr.sort(key=lambda x: (x, x == 0, x < 0))

    return arr


t = int(input())
while t > 0:
    n, m = map(int, input().split())
    arr = [int(i) for i in input().split()]

    result = process_sequence(arr, m)
    ##for num in result:
    ##print(num, end=' ')
    print(" ".join(map(str, result)))

    t -= 1
