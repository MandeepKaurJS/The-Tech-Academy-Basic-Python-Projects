user_number=int(input("Enter a Number from 1 to 7"))

#print("%s"%user_number)
days_list=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
if user_number==1:
    print(days_list[0])
elif user_number==2:
    print(days_list[1])
elif user_number==3:
    print(days_list[2])
elif user_number==4:
    print(days_list[3])
elif user_number==5:
    print(days_list[4])
elif user_number==6:
    print(days_list[5])
elif user_number==7:
    print(days_list[6])
else:
    print("None")
