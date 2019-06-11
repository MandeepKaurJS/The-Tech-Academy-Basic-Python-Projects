#Purpose: The Tech Academy- Python Course,creating our First Program together.
#demostrinf how to pass variable from to function

def start():
    print("Hello {} !".format(get_number()))
def get_number():
    number=12
    return number

if __name__=="__main__":
    start()