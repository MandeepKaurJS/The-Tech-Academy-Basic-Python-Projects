def my_square_root(input_number):
    square_root=input_number/2
    accuracy=0.001
    while abs(input_number-(square_root**2))>accuracy:
        square_root=(square_root+(input_number/square_root))/2
    return square_root
for x in range(1,21):
    y=my_square_root(x)
    print("squrae root of",x,"is",y)
    