#bad code
def f(x,y):
    z=x+y
    if z>100:
        print("yes")
    else:
        print("no")


#good practice
def is_sum_above(num1,num2,limit=100):
    total=num1+num2
    if total>limit:
        print("sum exceeds the limit")
    else:
        print("sum is within limit")

f(10,20)

is_sum_above(10,20)