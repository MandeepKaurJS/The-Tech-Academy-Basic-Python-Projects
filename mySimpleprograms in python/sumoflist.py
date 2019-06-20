def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

#print(listsum([1,3,5,7,9]))
def sum_of_list(mylist):
    list1=0
    for i in mylist:
        list1+=i
        ave=list1/len(mylist)
    return ave
print(sum_of_list([2,3,4,4]))
