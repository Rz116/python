import sys
import os.path
from os import path
def user():
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
    filename = username + ".doc"
                              
    length = len(username)
    if(length < 1):
        print("Type in a correct input")
        signup()
    else:
        fileexist = bool(path.exists(filename))
        if(fileexist == False):
            adminfile = open(filename, "x")
            adminfile.close()
            print("Login Created")
            getinfo()
        else:
            print("File already exists")
            
def getinfo():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    whichone = str(input("Which Deparment would you like to shop in: \n"
                                             "1.Fruit \n"
                                             "2.Poultry \n"
                                             "3.Meat \n"
                                             "4.Beverages \n"
                                             "5.Frozen Foods \n"
                                             "6.Dietry Food \n"
                                             "7.Kosher \n"
                                             "8. Halal \n"
                                             "9. Cart \n"
                                             "10.Exit the program\n"
                                             "Type in a number from 1-10 to select an option: "))
                                                                   
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
