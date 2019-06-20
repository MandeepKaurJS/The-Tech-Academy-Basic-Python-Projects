from math import*
def cal_math(x):
    y=sin(x)-cos(x)+sin(x)*cos(x)
    return y
print(cal_math(2))
def cal_math1(x):
    y=abs((x)**3)+(cos(sqrt(3*x)))
    return y
print(cal_math1(3))
def Distance(a,b):
    x1,y1,z1= a[0],a[1],a[2]
    x2,y2,z2=b[0],b[1],b[2]
    distance=sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
    return distance
#print(Distance(2,3,-5,4,-3,12))