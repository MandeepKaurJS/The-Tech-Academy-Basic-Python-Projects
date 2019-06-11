# testing purpose
mySentence='I love the color'
 
color_list=['Red','Blue','Green','Pink','Teal','Black']
def Color_function(name):
    lst=[]
    for i in color_list:
        msg ="{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

lst= Color_function("Mandeep")
for i in lst:
    print(i)
def printName():
    print("I absolutely \nlove coding \nwith Python!".format())
def getName(name = ""):
    name = askName(name)
    print("Thank you, welcome {}!".format(name))


def askName(name):
    go = True
    while go:
        if name == "":
            name = input("Please enter your name:\n>>> ")
            if name != "":
                go = False
                
    return name


if __name__ == '__main__':
    getName()

"""if __name__ == '__main__':
    printName()"""