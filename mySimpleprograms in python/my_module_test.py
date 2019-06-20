#import my_module
#import math
from my_module import add_fun,mul_fun
#from math import sqrt,sin
from math import*
a=5
b=6
#c=my_module.add_fun(a,b)
c=add_fun(a,b)
print(c)
#d=my_module.mul_fun(a,b)
d=mul_fun(a,b)
print(d)
#print(math.sqrt(4))
print(sqrt(4))
print(sin(2))