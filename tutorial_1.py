import os.path
from os import path

def main():
    filedir = os.path.dirname(os.path.realpath("__file__"))
    whichone = str(input("Which Deparment would you like to shop in: \n "
                                             "1.Fruit \n"
                                             "2.Poultry \n"
                                             "3.Meat \n"
                                             "4.Beverages \n"
                                             "5.Frozen Foods \n"
                                             "6.Dietry Food \n"
                                             "7.Kosher \n"
                                             "8. Halal \n"
                                             "9. Cart \n"
                                             "Type in a number from 1-8 to select an option: "))
                                                                   
    match(whichone):
        case "1":
            filepath = filedir + "\Fruit.py"
            
        case "2":
            filepath = filedir + "\Poultry.py"
            
        case "3":
            filepath = filedir + "\Meat.py"
            
        case "4":
            filepath = filedir  + "\Beverages.py"
            
        case "5":
            filepath = filedir + "\Frozen.py"
            
        case "6":
            filepath = filedir  + "\Dietry.py"
            
        case"7":
            filepath = filedir + "\Kosher.py"
            
        case "8":
            filepath = filedir  + "\halal.py"
            
        case "9":
            filepath = filedir + "\cart.py"
            
        case default:
            print("BIG BIG ISSUE BROTHER")
            main()
    
    filenamepath = {
            "__file__":filepath,
            "__name__":"__main__",
            }

    with open(filepath,"rb") as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);
    main()
    
if __name__ == "__main__":
    main()
