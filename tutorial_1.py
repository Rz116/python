import os.path
from os import path
def login():
    getinfo()
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
                                             "Type in a number from 1-9 to select an option: "))
                                                                   
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
            
        case default:
            print("Type in a correct input")
            main()
    
    filenamepath = {
            "__file__":filepath,
            "__name__":"__main__",
            }

    with open(filepath,"rb") as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);
    
def main():
    print("hello")
    login()
    
if __name__ == "__main__":
    main()
