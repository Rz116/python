import os.path
from os import path
def main():
    askinfo();
    
def askinfo():
    checkpoint = "askinfo";
    whichoption = str(input("1-Create a new file \n"
                            "2-Search for a new file\n"
                            "Select an option by typing 1 or 2: "));
    checkinfo(whichoption,checkpoint)
    
def checkinfo(optionwhich,pointcheck):
    match(pointcheck):
        case "askinfo":
            value = ord(str(optionwhich))
            if(int(value)) < int(49) or int((value) > int(50)):
                print("Incorrect input, Type in 1 or 2!");
                askinfo()
            else:
                print("You have selected a correct input");
        case default:
            print("Uh somethings wrong")

if __name__ == "__main__":
    main();
