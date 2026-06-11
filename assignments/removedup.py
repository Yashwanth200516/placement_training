def remove_duplicates(arr):
    new_arr=[]
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)

    return new_arr

arr=[1,1,2,3,4,4,5,5,6]
print(remove_duplicates(arr))

