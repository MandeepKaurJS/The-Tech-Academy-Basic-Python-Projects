def magnitude(vector):
    x=vector[0]
    y=vector[1]
    z=vector[2]
    magni= ((x**2)+(y**2)+(z**2))**(1/2)
    cnorm=x/magni
    cnormy=y/magni
    cnormz=z/magni
    return [cnorm,cnormy,cnormz]
print(magnitude([2,3,-4]))
