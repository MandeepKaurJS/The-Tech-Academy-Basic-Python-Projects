def smallest_num(list):
    small=list[0]
    for min in list:
        if min<small:
            small=min
    return small
print(smallest_num([1,2,3,-4,0]))
def largest_num(list):
    big=list[0]
    for max1 in list:
        if max1>big:
            big=max1
    return big
print(largest_num([1,2,3,-4,0,5]))
        
        