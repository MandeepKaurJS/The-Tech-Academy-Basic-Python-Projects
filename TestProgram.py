# testing purpose
mySentence='I love the color'
 
color_list=['Red','Blue','Green','Pink','Teal','Black']
def Color_function(name):
    for i in color_list:
        print("{} {} {}".format(name,mySentence,i))

Color_function("deep")