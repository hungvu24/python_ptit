def generate_permutations(s, current_permutation, used, result):
    if len(current_permutation) == len(s):
        result.append(''.join(current_permutation))
        return

    for i in range(len(s)):
        if not used[i]:
            # Chọn một ký tự chưa được sử dụng
            used[i] = True
            current_permutation.append(s[i])

            # Gọi đệ quy để sinh hoán vị tiếp theo
            generate_permutations(s, current_permutation, used, result)

            # Quay lui: bỏ ký tự đã chọn để thử ký tự khác
            used[i] = False
            current_permutation.pop()

def print_lexicographic_permutations(s):
    result = []
    used = [False] * len(s)
    generate_permutations(s, [], used, result)

    return result
s = input()
print(print_lexicographic_permutations(s))