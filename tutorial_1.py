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
def logger(nameuser):
    names = []
    namefile = "username.doc"
    filedir = os.path.dirname(os.path.realpath("__file__"))
    admin = open(namefile, "r")
    adminvalue = admin.read().splitlines()

    for i in range(0,len(adminvalue)):
        names.append(adminvalue[i].strip())

    if nameuser not in names:
        print("Username doesnt exist!!")
        logger(nameuser)
    else:
        options = str(input("1. Check your cart \n"
                                           "2. Shop at more departments \n"
                                           "Type in 1 or 2 to select an option: "))
        length = len(options)
        if(length < 1 or length > 1):
            print("Type in a corect input")
            logger(nameuser)
        else:
            match (int(options)):
                case 1:
                    adminfile = open(filename, "r")
                    print("------Reciept------")
                    print(adminfile.read())
                    adminfile.close()
                case 2:
                    getinfo(nameuser)
                case default:
                    print("Type in a correcet input")
                    logger(nameuser)
        
def signup(nameof_file):
    usernames = []
    filedir = os.path.dirname(os.path.realpath("__file__"))
    username = str(input("Create a username:  "))
    length = len(username)
    if(length < 1):
        print("Type in a correct input")
        signup(nameof_file)
    else:
        adminfile = open(nameof_file, "r")
        adminvalue = adminfile.read().splitlines()
        adminfile.close()
        for i in range(len(adminvalue)):
            usernames.append(adminvalue[i].strip())
        adminfile.close()

        if username in usernames:
            print("The username already exists")
            logger(username)
        else:
            adminfile = open(nameof_file, "a")
            adminfile.write(username + "\n")
            adminfile.close()
            getinfo(username)
        
def getinfo(name):
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    print("----Departments----")
    departments = ["1.Fruit","2.Poultry","3.Meat","4.Beverages","5.Frozen Foods",
                                "6.Dietry Food","7.Kosher","8.Halal","9.Cart/Reciept","10.Exit the Program","11.Sign out"]
    for i in range(0,len(departments)):
        print(departments[i])
    whichone = str(input("Type in a number from 1-11 to select an option Department: "))
                                                                   
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
            filename = name + ".doc"
            fileexist = bool(path.exists(filename))
            if(fileexist == False):
                print("You must shop first to view cart")
                getinfo(name)
            else:               
                admin = open(filename, "r")
                print("------Reciept------")
                print(admin.read())
        case "10":
            print("Goodbye")
            sys.exit()
        case "11":
            print("Signing out")
            user()

        case default:
            print("Type in a correct input")
            getinfo()
    
    filenamepath = {
            "__file__":filepath,
            "__name__":"__main__",
            }

    with open(filepath,"rb") as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);
        
    getinfo(name)
    
def main():
    user()
    
if __name__ == "__main__":
    main()
