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