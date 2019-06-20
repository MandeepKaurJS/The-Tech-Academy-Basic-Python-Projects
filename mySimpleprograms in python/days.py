user_number=int(input("Enter a Number from 1 to 7"))

#print("%s"%user_number)
days_list=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]

if user_number == 1:
     print(days_list[0])

elif user_number == 2:

    print("TUSEDAY")
elif user_number == 3:

    print("WEDNESDAY")
elif user_number == 4:

    print("THURSDAY")
elif user_number == 5:

    print("FRIDAY")
elif user_number == 6:

    print("SATURDAY")
elif user_number == 7:

    print("SUNDAY")
else:
    print("out of order")
