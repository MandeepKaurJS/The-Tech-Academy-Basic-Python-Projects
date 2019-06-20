#Calculate Wage
n=int(input("Enter your hours per week"))
if(n<0) or (n>168):
    print("INVALID")
elif(n<=40):
        total=(n*8)
        print("YOU MADE",total,"DOLLARS THIS WEEK")
elif(41<=n<=50):
    total=(40*8)+(n-40)*9
    print("YOU MADE",total,"DOLLARS THIS WEEK")
elif(n>51):
    total=(n-41)*10+(40*8)
    print("YOU MADE",total,"DOLLARS THIS WEEK")
else:
          print("")

