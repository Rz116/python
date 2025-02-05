import os.path
from os import path
import sys
msg = ["New file name: ","Existing File Name: "]

def main():
    askinfo();
    
def askinfo():
    global whichoption
    checkpoint = "askinfo";
    whichoption = str(input("1-Create a new file \n"
                            "2-Search for a file\n"
                            "3-Exit the program\n"
                            "Select an option by typing 1,2 or 3: "));
    checkinfo(whichoption,checkpoint)
    
def typefile():
    checkpoint = "typefile"
    if(int(whichoption) == int(1)):
        typeof = str(input("What type of file would you like to create\n"
                           "1-Excel File\n"
                           "2-Word Document\n"
                           "3-Text File\n"
                           "Select an option by typing in 1,2 or 3: "))
        checkinfo(typeof,checkpoint)
    else:
        typeof = str(input("What file would you like to open?\n"
                           "1-Excel File\n"
                           "2-Word Document\n"
                           "3-Text File\n"
                           "Select an option by typing in 1,2 or 3: "))
        checkinfo(typeof,checkpoint)
            
def files():
    checkpoint = "files"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(whichone))

    if(fileexist == True):
        adminfile = open(whichone, "r")
        print(adminfile)
        
    else:
        adminfile = open(whichone,"x")
        print("File created")

    adminfile.close()
    program()
def program():
    checkpoint = "program"
    programcontinue = str(input("1-Create more files \n"
                                "2-Stop the program \n"
                                "Type in 1 or 2 to select a choice: "))
    checkinfo(programcontinue,checkpoint)

def checkinfo(optionwhich,pointcheck):
    global whichone
    match(pointcheck):
        case "askinfo":
            value = ord(str(optionwhich))
            if(int(value)) < int(49) or int((value) > int(51)):
                print("Incorrect input, Type in 1,2 or 3!");
                askinfo()
            else:
                match int(optionwhich):
                    case 1:
                        whichone = str(input(msg[0]));
                        typefile()
                    case 2:
                        whichone = str(input(msg[1]));
                        typefile()
                    case 3:
                        print("Goodbye!!!")
                        sys.exit()
                    case default:
                        print("You did something very wrong to be here")
                        sys.exit()
        case "typefile":
            check = ord(str(optionwhich))
            if(int(check)) < int(49) or int((check) > int(51)):
                print("Type in a correcet input")
                typefile()
            else:
                match int(optionwhich):
                    case 1:
                        whichone = whichone + ".xlsx"
                        files()
                    case 2:
                        whichone = whichone + ".doc"
                        files()
                    case 3:
                        whichone = whichone + ".txt"
                        files()
                    case default:
                        print("You did something very wrong to be here")
                        sys.exit()
        case "program":
            check2 = ord(str(optionwhich))
            if(int(check2)) < int(49) or int((check2) > int(50)):
                print("Type in a correct input")
                files()
            else:
                if(int(optionwhich) == int(1)):
                    askinfo()
                else:
                    print("Goodbye!!")
                    sys.exit()
        case default:
            print("Uh somethings wrong")
            sys.exit()
            
if __name__ == "__main__":
    main();
