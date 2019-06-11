##print(dir(str))
##print(help(str))
import os
#print(os.getcwd())
def writeData():
    data='Hello world !'
    #open and appending data at the end of file by using a
    with open('TestPy.txt','a') as f:
        f.write(data)
        f.close()
        
def openFile():
    with open('TestPy.txt','r') as f:
    #what we read from file by using this read method 
        data=f.read()
        # then print what inside the file
        print(data)
        #close our file using close method()
        f.close()
if __name__=="__main__":
    writeData()
    openFile()