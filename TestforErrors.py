def getInfo():
    var1=input("Please provide the first numeric value: ")
    var2=input("Please provide the second numeric value: ")
    Compute(var1,var2)
    
def Compute(var1,var2):
    try:
        var3=int(var1) + int(var2)
        print("{} + {} ={}".format(var1,var2,var3))
    except ValueError as e:
        print("{}: \n You did not provide a numeric value".format(e))
    except:
        print("oops, you  provided invalid input, program will close!")
    finally:
        print("Moving on ....")
if __name__ == "__main__":
    getInfo()