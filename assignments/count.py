def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count

print(count_occurrences([1, 2, 3, 4, 4, 5, 4, 5], 4)) 

