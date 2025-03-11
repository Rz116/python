import os.path
from os import path
import sys

def getinfo():
    global fruit,items,pounds,amount
    counter = 0
    fruit = ["1. Apples $3.00/lb ","2. Banana $2.50/lb","3. Peaches $3.50/lb","4. Oranges $3.00/lb",
                  "5. Mangos $4.00/lb","6. Pears $5.00/lb","7. Guava $3.00/lb","8. Kiwi $2.50/lb"]
    items = []
    pounds = []
    
    print("FRUIT DEPARTMENT: ")
    fruitlength = len(fruit)
    for i in range(0,int(fruitlength)):
        print(fruit[i])
        
    amount = str(input("How many items would you like to buy (Type in a number between 1 and 8!): "))
    length_input1 = len(amount)
    info = list(amount)
    if(length_input1 > 1 or length_input1 < 1):
        print("Type in a correct input!")
        getinfo()
    else:
        checkinput = ord(amount)
        if(checkinput < 49 or checkinput > 56):
            print("Type in a correct input")
            getinfo()
        else:
            Getitems(counter)

def Getitems(counter2):
    global items,temporary
    counter3 = 0
    whichone = str(input("Which item would you like to add to cart(Type a number from 1-8): "))
    length = len(whichone)
    if(length < 1 or length > 1):
        print("Type in a correct input")
        Getitems(counter2)
    else:
        checkinput = ord(whichone)
        if(checkinput < 49 or checkinput > 56):
            print("Type in a correct input")
            Getitems(counter2)
        else:
            items.append(whichone)
            counter2 = counter2 + 1
            if(counter2 == int(amount)):
                temporary = items
                info2(counter3)
            else:
                temporary = items
                Getitems(counter2)
    
def info2(counterthree):
    howmuch = str(input("How many pounds of item " + temporary[counterthree ] + " would you like to buy: "))
    length = len(howmuch)
    check2 = list(howmuch)
    if(length < 1):
        print("Type in a correct input")
        info2(counterthree)
    else:        
        check3 = howmuch.isdigit()
        if(check3 == False):
            print("Type in a correct input")
            info2(counterthree)
        else:             
            pounds.append(howmuch)
            counterthree = counterthree + 1
            if(counterthree == int(amount)):
                cartinfo()
            else:
                info2(counterthree)
    
def cartinfo():
    global totals
    print(pounds)
    print(items)
    prices = []
    totals = []
    for i in range(0,len(items)):
        whichitem = items[i]
        match(whichitem):
            case "1":
                prices.append(3)
            case "2":
                prices.append(2.5)
            case "3":
                prices.append(3.5)
            case "4":
                prices.append(3)
            case "5":
                prices.append(4)
            case "6":
                prices.append(5)
            case "7":
                prices.append(3)
            case "8":
                prices.append(2.5)
            case default:
                print("Something went wrong")
                sys.exit
    for i in range(0,len(prices)):
        itemtotal = float(prices[i]) * float(pounds[i])
        totals.append(itemtotal)
    
    print(prices)
    print(totals)
    cart()
def cart():
    global usernames
    counter = 0
    usernames = []
    adminfile = open("username.doc", "r")
    adminvalue = adminfile.read().splitlines()
    adminfile.close()
    
    for i in range(len(adminvalue)):
        usernames.append(adminvalue[i].strip())
    for i in range(len(usernames)):
        print(str(i +1) + ". " + usernames[i])
        
    username = str(input("What is your username: "))
    length = len(username)
    check(length,username,counter)

def check(leng,nameuser,counter1):
    filedir = os.path.dirname(os.path.realpath("__file__"))
    if(leng < 1 ):
        print("Type in a correct input")
        cart()
    else:
        if nameuser not in usernames:
            print("Type in a correct input")
            cart()

        filename = nameuser + ".doc"
        fileexist = bool(path.exists(filename))
        if(fileexist == False):
            adminfile = open(filename,"x")
            write(filename)
        else:
            #VERY IMPORTANT SHIT TO DO HERE
            print("IMMA DO THIS PART LATER")
def write(namefile):
    total = 0
    products = []
    adminfile = open(namefile,"a")
    adminfile.write("Products and Price" + "\n" + "\n")
    for i in range(0,len(items)):
        match(items[i]):
            case "1":
                products.append("Apples")
            case "2":
                products.append("Bananas")
            case "3":
                products.append("Peaches")
            case "4":
                products.append("Oranges")
            case "5":
                products.append("Mangos")
            case "6":
                products.append("Pears")
            case "7":
                products.append("Guava")
            case "8":
                products.append("Kiwi's")
            case default:
                print("Theres a big problem")
                sys.exit()
    
    for i in range(0,len(products)):
        adminfile.write(str(pounds[i]) + " Lbs " + products[i] +  " $"+  str(totals[i]) + "\n")
    for i in range(0,len(totals)):
        total = total + totals[i]
    adminfile.write("\n"+ "Total Price: " + " $" + str(total))
    adminfile.close()

    ask(namefile)
def ask(filename):
    program = str(input("1. Look at your receipt \n"
                                         "2. Shop at another department \n"
                                         "3. Exit the program \n"
                                         "Type in 1, 2 or 3 to select an option: "))
    length = len(program)
    if (length < 1 or length > 1):
        print("Type in a correct input")
        ask(filename)
    else:
        char = ord(program)
        if(char < 49 or char > 51):
            print("Type in a correct input")
            ask()
        else:
            match(int(program)):
                case 1:
                    adminfile = open(filename, "r")
                    print("----Reciept----")
                    print(adminfile.read())
                    adminfile.close()
                case 2:
                    print("Please select a department")
                case 3:
                    print("Thank you for shopping!!")
                    sys.exit()
                case default:
                    print("PROBLEM")
                    sys.exit()
                
    
def main():
    getinfo()

if __name__ == "__main__":
    main()
