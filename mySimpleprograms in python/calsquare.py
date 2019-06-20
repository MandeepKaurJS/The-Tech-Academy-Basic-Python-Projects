#calculate square root
user_response=float(input("enter a number"))
guess=user_response/2
accuracy=0.01
x=0
while abs(user_response-(guess**2))>accuracy:
    print("iteration:",x,"guess",guess)
    guess=(guess+(user_response/guess))/2
    x=x+1
    print("original number",user_response)
    print("square root of number",guess)