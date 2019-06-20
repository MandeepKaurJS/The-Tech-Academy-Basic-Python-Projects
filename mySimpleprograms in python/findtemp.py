user_response=input("please input temprature in celsius")
celsius=float(user_response)
fahrenheit=((celsius*9)/5)+32
print(" the temprature is",fahrenheit,"degree fahrenheit")
if fahrenheit<32:
    print("it is freezing")
elif fahrenheit<50:
    print("it is chilly")    
elif fahrenheit<90:
    print("it is ok:")
else:
    print("it is  hot")
