def remaining_loan(principal,interest_rate, duration ,payment):
   if interest_rate==0:
        return principal*(1-payment/n)
   n=duration*12
   r=interest_rate/100/12
   m=1+r
   remaining=principal*((m**n)-(m)**payment)/((float(m)**n)-1)
   return remaining
print(remaining_loan(1000.0,4.5,5,12))