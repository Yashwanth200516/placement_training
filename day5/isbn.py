
def binary_search(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1

# isbn=[1,2,3,4,5,6]
# target=4

# print(binary_search(isbn,target))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            
        arr[j+1]=key

    return arr

products=[1005,1001,1020,1015,1010,1025]
target=1015
print(products)
print(insertion_sort(products))
print(binary_search(products,target))