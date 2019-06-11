import os,time
# open a file
fpath="C:\\Users\\VrinMan Dulay\\Documents\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\"
dirs=os.listdir(fpath)
#this would print all the files and directories
print("List of files and folders: \n")
for file in dirs:
    print(file)
    
    if file.endswith(".txt"):
        print("Files end with txt")
        show=os.path.join(fpath,file)
        print(show)
        showtime=time.ctime(os.path.getmtime(show))
        print(showtime)

#use the path.join() method from the OS module to concatenate the file name to its file path,
#forming an absolute path.
fname='TextPy.txt'
fpath='C:\\Users\\VrinMan Dulay\\Documents\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\'


abpath=os.path.join(fpath,fname)
print("Showing Absalute path of file \n")
print(abpath)
# getmtime method
print("Last modified: %s" % time.ctime(os.path.getmtime(fpath)))
#print(os.path.getmtime('C:\\Users\\VrinMan Dulay\\Documents\\GitHub\\The-Tech-Academy-Basic-Python-Projects\\TextPy.txt'))

#print each file with txt