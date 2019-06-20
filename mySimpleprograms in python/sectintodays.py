time = int(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print(day,"days",hour,"hours",minutes,"minutes",time,"seconds")

    
