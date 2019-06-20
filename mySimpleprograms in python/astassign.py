#assignment
def triangle_value(n):
    for i in range(0,n):
        print("*"*i)
    for j in range(n,0,-1):
        print("*"*j)  
print(triangle_value(8))
def start():
    f_name="Mandeep"
    l_name="kaur"
    age=26
    gender="female"
    get_Info(f_name,l_name,age,gender)
    
def get_Info(f_name,l_name,age,gender):
    print("My name is {} {}. I am {} Yearold {}.".format(f_name,l_name,age,gender))
    class Greetings:
        def myMethod1(self):
            print('Hello world!')

        def myMethod2(self):
            print('Hello Python!')

        def myMethod3(self):
            print('Hello Tech Academy!')
