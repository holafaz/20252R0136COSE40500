def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

nums = [4, 2, 7, 1, 9]
print(linear_search(nums, 7))
