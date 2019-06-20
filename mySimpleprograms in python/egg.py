from datetime import datetime

my_date = raw_input("Enter B'date in mmi/dd/yyyy format:")

b_date = datetime.strptime(my_date, '%m/%d/%Y')

print "Age : %d" % ((datetime.today() - b_date).days/365)
