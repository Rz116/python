import sys
import os.path
from os import path

def user():
    namefile = "username.doc"
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
            user()
        else:
            if(int(logon) == 1):
                username = str(input("What is your username: "))
                length2 = len(username)
                if(length2 < 1):
                    print("Type in a correct input")
                    user()
                else:
                    login(username)
            else:
                signup()
def login(nameuser):
    filedir = os.path.dirname(os.path.realpath("__file__"))
    filename = nameuser + ".doc"
    fileexist = bool(path.exists(filename))
    if(fileexist == True):
        print("Logged on !")
    else:
        print("Username doesnt exist")
        signup()
def signup():
    filedir = os.path.dirname(os.path.realpath("__file__"))
    username = str(input("Create a username: "))
    filesignup = username + ".doc"
                              
    length = len(username)
    if(length < 1):
        print("Type in a correct input")
        signup()
    else:
        fileexist = bool(path.exists(filesignup))
        if(fileexist == False):
            adminfile = open(filesignup, "x")
            adminfile.close()
            print("Login Created")
            getinfo(filesignup)
        else:
            print("File already exists")
            
def getinfo(usernamefile):
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
    main()
    
def main():
    user()
    
if __name__ == "__main__":
    main()
