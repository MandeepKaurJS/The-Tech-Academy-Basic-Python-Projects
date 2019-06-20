from math import*
def even_only(mylist):
    evens=[]
    for num in mylist:
        if num%2==0:
            evens.append(num)
    return evens

print(even_only([1,3,5,7,9,8,6]))
def odd_only(mylist):
    odds=[]
    sum=0
    num=1
    for num in mylist:
        if num%2!=0:
            sum=sum+num
            odds.append(num)
        num=num+1
    return sum
#print(odd_only([2,4,3,5]))
def perfect_num(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        return (True)
    else:
        return (False)
print(perfect_num(6))
def prime_num(n):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                return(False)
        else:
            return(True)
    else:
        return(False)
print(prime_num(407))
def lcm_fun(x,y):
    if x>y:
        m=x
    else:
        m=y
    while(True):
        if(m%x==0)and(m%y==0):
            lcm_fun=m
            break
        m+=1
    return lcm_fun
print(lcm_fun(4,6))
    