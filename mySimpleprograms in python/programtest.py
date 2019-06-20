name="python"
def getName():
    name="C#"
    print("I am coding with {} ".format(name))
    
getName()
progName = "Python"
answer = "I love {}!".format(progName)
print(answer)

num1 = 3
num2 = 1
answer = 'The answer is {}.'.format(num1 + num2)
print(answer)

truth1 = True
truth2 = False
print("The truth is always {}.".format(truth2))
colorList = ('Pink','Black','Neon Green','Teal','Red')
myString = 'I love the color {}.'.format(colorList[2])
print(myString)
#for loop
i=0
for i in range(10):
    print("{} Iteration through the for loop.".format(i))
    i+=1
#while loop
j=0
while j<10:
    print("{} Iteration through the while loop.".format(j))
    j += 1
# if and elseif statements
num1=12
key=True
if(num1==12):
    if key:
        print('num1 is equal to twelve! and they have th key')
    else:
        print('num1 is equal to twelve! and they dont have the key')
elif (num1 < 10):
    print('num 1 is less than twelve')
else:
    print('num1 is not equal to twelve!')
#complex code for loop
mySentence ="loves the color"
color_list=['red','blue','green','pink','teal','black']
def color_function(name):
    lst=[]
    for i in color_list:
        msg="{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst
def get_name():
    go=True
    while go:
        
        name=input('What is your name:')
        if name =='':
            print("you need to provide your name")
        elif name=="deep":
            print("Deep you may not use this software.")
        else:
            go= False
    lst=color_function(name)
    for i in lst:
        print(i)
get_name()

#testing

num1 = 6
num2 = 10

if num1 < num2:
    print("less than")
elif num1 == num2:
    print("equal to")
else:
    print("greater than")
    
#name
def getName():
	fName = input("Please type in your first name without any capitalizations.\n>>> ").lower()
	print("Thank you {}, welcome back!".format(fName))
getName()
    
	