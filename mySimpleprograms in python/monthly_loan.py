#total loan amnt
principal=4059.23
#annunal interest rate
interest_rate=500.12
#loan duration in years
duration=2
def monthly_loan(principal,interest_rate,duration):
    if interest_rate==0:
        return principal/n
    n=duration*12
    r=interest_rate/(100*12)
    monthly_payment=principal*((r*((r+1)**n))/(((r+1)**n)-1))
    return monthly_payment