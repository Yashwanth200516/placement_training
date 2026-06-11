ids=[101,205,310,415,520]
target=410


def lin_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1


# print(lin_search(ids,target))

vehicles=["KA01AB1234","KA05XY7890","KA03MN4567","KA09PQ1111"]
find="KA03MN4567"

print(lin_search(vehicles,find))

