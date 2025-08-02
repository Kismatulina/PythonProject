# TASK1 HW3

begin_arr = [1, 2, 2, 2, 3, 4, 5, 9, 9, 9]

duplicate_val = begin_arr[0]

total_arr = [duplicate_val]
count = 0

for i in range(len(begin_arr)):

    if begin_arr[i] == duplicate_val:
        count += 1
    else:
        duplicate_val = begin_arr[i]
        total_arr.append(duplicate_val)


print("New array: ", total_arr)