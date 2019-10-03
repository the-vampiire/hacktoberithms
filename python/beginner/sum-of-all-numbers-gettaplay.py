def sum_all(li):
    a=min(li)
    b=max(li)
    n=b-a+1
    return (n*(a+b)/2)
print(sum_all([1,4]))
print(sum_all([4,1]))
print(sum_all([10,15]))
