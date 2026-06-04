def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            
        arr[j+1]=key

    return arr

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

arr=list(map(int,input().split()))
insertion_sort(arr)
print(arr)
target=int(input("Enter the element to search:"))


res=binary_search(arr,target)

if res!=-1:
    print(f"Element is found at index :{res}")
else:
    print("element not found")