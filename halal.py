import os.path
from os import path
import sys

def getinfo():
    global fruit,items,pounds,amount
    counter = 0
    poultry = []
    price = []
    items = []
    pounds = []
    
    admin = open("halal.txt", "r")
    adminvalue = admin.read().split(",")
    print("POULTRY DEPARTMENT: ")
    fruitlength = len(adminvalue)
    for i in range(0,int(fruitlength)):
        poultry.append(adminvalue[i].strip())
    admin.close()

    admin2 =  open("halaPrice.txt","r")
    adminvalue2 = admin2.read().split(",")
    for i in range(len(adminvalue2)):
        price.append(adminvalue2[i].strip())
        
    for i in range(0,len(poultry)):
        print(str(i+1) + ". " + poultry[i] + "  " + price[i])

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
    prices = []
    totals = []
    for i in range(0,len(items)):
        whichitem = items[i]
        match(whichitem):
            case "1":
                prices.append(3.5)
            case "2":
                prices.append(4.5)
            case "3":
                prices.append(12)
            case "4":
                prices.append(3)
            case "5":
                prices.append(3.5)
            case "6":
                prices.append(5)
            case "7":
                prices.append(6)
            case "8":
                prices.append(8)
            case default:
                print("Something went wrong")
                sys.exit
    for i in range(0,len(prices)):
        itemtotal = float(prices[i]) * float(pounds[i])
        totals.append(itemtotal)
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
    existing(length,username,counter)

def existing(leng,nameuser,counter1):
    filedir = os.path.dirname(os.path.realpath("__file__"))
    if(leng < 1 ):
        print("Type in a correct input")
        cart()
    else:
        if nameuser not in usernames:
            print("Type in a correct input")
            cart()
        else:            
            filename = nameuser + ".doc"
            fileexist = bool(path.exists(filename))
            if(fileexist == False):
                price = nameuser + "prices" + ".doc"
                product = nameuser + "product" + ".doc"
                pound = nameuser + "pound" + ".doc"
                prices = open(price, "x")
                adminfile = open(filename,"x")
                write(filename,price,product,pound)
            else:
                exists(nameuser,filename)
def exists(username,namefile):
    total = 0
    sums = []
    products = []
    products2 = []
    pounds2 = []
    filedir = os.path.dirname(os.path.realpath("__file__"))
    price = username + "prices" + ".doc"
    produce = username + "product" + ".doc"
    lbs = username + "pound" + ".doc"
    fileexists = bool(path.exists(price))
    fileexists2 = bool(path.exists(produce))
    fileexists3 = bool(path.exists(lbs))
    if(fileexists == False or fileexists2 == False or fileexists3 == False):
        print("Something went wrong")
        sys.exit()
    else:
        adminproducts = open(produce,  "a")
        adminprices = open(price, "a")
        adminpounds = open(lbs, "a")
    for i in range(len(items)):
        match(items[i]):
            case "1":
                products2.append("Turkey Bacon")
            case "2":
                products2.append("Halal Chicken Thighs")
            case "3":
                products2.append("Halal Steak")
            case "4":
                products2.append("Ground Beef")
            case "5":
                products2.append("Lamb Chop")
            case "6":
                products2.append("Halal Chicken Thighs")
            case "7":
                products2.append("Ground Lamb")
            case "8":
                products2.append("Salmon")
            case default:
                print("Theres a big problem")
                sys.exit()
                
    for i in range(len(products2)):
        adminproducts.write(products2[i] + "\n")
    adminproducts.close()
    for i in range(len(totals)):
        adminprices.write(str(totals[i]) + "\n")
    adminprices.close()
    for i in range(len(pounds)):
        adminpounds.write(str(pounds[i]) + "\n")
    adminpounds.close()

    adminproducts2 = open(produce, "r+")
    adminvalue1 = adminproducts2.read().splitlines()
    adminproducts2.close()
    for i in range(len(adminvalue1)):
        products.append(adminvalue1[i].strip())
        
    adminprices2 = open(price,"r")
    adminvalue2 = adminprices2.read().splitlines()
    adminprices2.close()
    for i in range(len(adminvalue2)):
        sums.append(adminvalue2[i].strip())
        
    adminpounds2 = open(lbs, "r")
    adminvalue3 = adminpounds2.read().splitlines()
    adminpounds2.close()
    for i in range(len(adminvalue3)):
        pounds2.append(adminvalue3[i].strip())

    for i in range(len(sums)):
        total = total + float(sums[i])
        
    adminfile = open(namefile , "w")
    adminfile.write("Products and Prices" + "\n" + "\n")
    for i in range(0,len(pounds2)):
        adminfile.write(str(pounds2[i]) + " Lbs " + str(products[i]) + "  $" + str(sums[i]) + "\n")
    adminfile.write("\n" + "Total price:  " + " $"  + str(total))
    adminfile.close()
    ask(namefile)
    
def write(namefile,prices,item,lbs):
    total = 0
    products = []
    adminfile = open(namefile,"a")
    adminother = open(prices, "a")
    adminother2 = open(item, "a")
    adminother3 = open(lbs, "a")
    adminfile.write("Products and Price" + "\n" + "\n")
    for i in range(0,len(items)):
        match(items[i]):
            case "1":
                products.append("Turkey Bacon")
            case "2":
                products.append("Halal Chicken Thighs")
            case "3":
                products.append("Halal Steak")
            case "4":
                products.append("Ground Beef")
            case "5":
                products.append("Lamb Chop")
            case "6":
                products.append("Halal Chicken Thighs")
            case "7":
                products.append("Ground Lamb")
            case "8":
                products.append("Salmon")
            case default:
                print("Theres a big problem")
                sys.exit()
    
    for i in range(0,len(products)):
        adminfile.write(str(pounds[i]) + " Lbs " + products[i] +  " $"+  str(totals[i]) + "\n")
        adminother.write(str(totals[i]) + "\n")
        adminother2.write(str(products[i]) + "\n")
        adminother3.write(str(pounds[i]) + "\n")
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
