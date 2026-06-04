def get_ele(arr):
    print(arr[0])   #O(1)

def print_all(arr):
    for i in arr:   #O(N)
        print(i)
    print()

def print_pairs(arr):
    for i in arr:           
        for j in arr:     #O(N^2)
            print(i,j)
        print()


get_ele([1,2,3,4,5,6])
print_all([1,2,3,4,5,6])
print_pairs([1,2,3,4,5,6])