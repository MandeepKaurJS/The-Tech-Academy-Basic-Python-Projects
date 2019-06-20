principal=float(input("Enter loan amount: "))
interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))
def monthly_loan(principal,interest_rate,duration):
    if interest_rate==0:
        return principal/n
    n=duration*12
    r=interest_rate/100/12
    monthly_payment=principal*((r*((r+1.0)**n))/(((r+1.0)**n)-1.0))
    return monthly_payment
def remaining_loan(principal,interest_rate, duration ,payment):
   if interest_rate==0:
        return principal*(1-payment/n)
   n=duration*12
   r=interest_rate/100/12.0
   m=1.0+r
   remaining=principal*((m)**n-(m)**payment)/((float(m)**n)-1.0)
   return remaining
monthly = monthly_loan(principal,interest_rate,duration)

print("LOAN AMOUNT:",int(principal)," INTEREST RATE: ",int(interest_rate))

print("DURATION (YEARS): ",duration," MONTHLY PAYMENT: ",int(monthly))

for x in range(1,duration+1):
    mon = x*12
    rem = remaining_loan(principal,interest_rate,duration,mon)
    print("YEAR: ",int(x)," BALANCE: ",int(rem)," TOTAL PAYMENT: ",int(monthly*mon))
