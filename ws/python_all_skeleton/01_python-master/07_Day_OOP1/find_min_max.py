# 최소값 찾기
lst = [3, 2, 7, 1, 5]

min_val = lst[0]
max_val = lst[0]

for val in lst: 
    if min_val > val:
        min_val = val

    if max_val < val:
        max_val = val

print(min_val, max_val)

