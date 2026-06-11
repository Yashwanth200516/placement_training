def largest(arr):
    maxi=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]

    return maxi

sales=list(map(int,input().split()))

print(largest(sales))