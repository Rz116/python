import os.path
from os import path

msg = ["New file name: ","Existing File Name: "]
def main():
    askinfo();
    
def askinfo():
    checkpoint = "askinfo";
    whichoption = str(input("1-Create a new file \n"
                            "2-Search for a new file\n"
                            "Select an option by typing 1 or 2: "));
    checkinfo(whichoption,checkpoint)
    
def checkinfo(optionwhich,pointcheck):
    global whichone
    match(pointcheck):
        case "askinfo":
            value = ord(str(optionwhich))
            if(int(value)) < int(49) or int((value) > int(50)):
                print("Incorrect input, Type in 1 or 2!");
                askinfo()
            else:
                if(int(optionwhich) == int(1)):
                    whichone = str(input(msg[0]));
                else:
                    whichone = str(input(msg[1]));
                whichone = whichone + ".doc";
                files()
        case default:
            print("Uh somethings wrong")

def files():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(whichone))

    if(fileexist == True):
        adminfile = open(whichone, "r")
        print(adminfile)
    else:
        adminfile = open(whichone,"x")
        print("File created")

    adminfile.close()
    

if __name__ == "__main__":
    main();
