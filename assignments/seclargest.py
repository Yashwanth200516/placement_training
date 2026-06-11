def second_larget(arr):
    max1=arr[0]
    max2=float('-inf')

    for i in range(len(arr)):
        if arr[i]>max1:
            max2=max1
            max1=arr[i]
        elif arr[i]>max2 and arr[i]!=max1:
            max2=arr[i]

    return max2

arr=[89,10,20,88,90,30,100,40,50]
print(second_larget(arr))
