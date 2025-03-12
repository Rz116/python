import sys
import os.path
from os import path

def user():
    filedir = os.path.dirname(os.path.realpath("__file__"))
    namefile = "username.doc"
    fileexist = bool(path.exists(namefile))
    if (fileexist == False):
        adminfile = open(namefile, "x")
        login(namefile)
    else:
        login(namefile)
        
def login(filename):
    filedir = os.path.dirname(os.path.realpath("__file__"))
    logon = str(input("1.Login \n"
                                   "2.Sign up \n"
                                   "Choose an option by typing in 1 or 2: "))
    length = len(logon)
    if(length < 1 or length > 1):
        print("Type in a correct input")
        user()
    else:
        checkinput = ord(logon)
        if(checkinput < 49 or checkinput > 50):
            print("Type in a correct input")
            login()
        else:
            if(int(logon) == 1):
                username = str(input("What is your username: "))
                length2 = len(username)
                if(length2 < 1):
                    print("Type in a correct input")
                    user()
                else:
                    logger(username)
            else:
                signup(filename)
def logger(username):
    print("I went to the logon page")
    getinfo()
def signup(nameof_file):
    filedir = os.path.dirname(os.path.realpath("__file__"))
    username = str(input("Create a username:  "))
    length = len(username)
    if(length < 1):
        print("Type in a correct input")
        signup(nameof_file)
    else:
        adminfile = open(nameof_file, "a")
        adminfile.write(username + "\n")
        adminfile.close()
        getinfo()
    
def getinfo():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    print("----Departments----")
    departments = ["1.Fruit","2.Poultry","3.Meat","4.Beverages","5.Frozen Foods",
                                "6.Dietry Food","7.Kosher","8.Halal","9.Cart/Reciept","10.Exit the Program"]
    for i in range(0,len(departments)):
        print(departments[i])
    whichone = str(input("Type in a number from 1-10 to select a Department: "))
                                                                   
    match(whichone):
        case "1":
            filepath = fileDir + "\Fruit.py"
            
        case "2":
            filepath = fileDir + "\Poultry.py"
            
        case "3":
            filepath = fileDir + "\Meat.py"
            
        case "4":
            filepath = fileDir  + "\Beverages.py"
            
        case "5":
            filepath = fileDir + "\Frozen.py"
            
        case "6":
            filepath = fileDir  + "\Dietry.py"
            
        case"7":
            filepath = filedir + "\Kosher.py"
            
        case "8":
            filepath = fileDir  + "\halal.py"
            
        case "9":
            filepath = fileDir + "\cart.py"
        case "10":
            print("Goodbye")
            sys.exit()
        case default:
            print("Type in a correct input")
            getinfo()
    
    filenamepath = {
            "__file__":filepath,
            "__name__":"__main__",
            }

    with open(filepath,"rb") as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);
        
    getinfo()
    
def main():
    user()
    
if __name__ == "__main__":
    main()
