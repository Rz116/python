import os.path
from os import path
def getinfo():
    global fruit,items,pounds,amount
    fruit = ["1. Apples $3.00/lb ","2. Banana $2.50/lb","3. Peaches $3.50/lb","4. Oranges $3.00/lb",
                  "5. Mangos $4.00/lb","6. Pears $5.00/lb","7. Guava $3.00/lb","8. Kiwi $2.50/lb"]
    pounds = []
    print("FRUIT DEPARTMENT: ")
    fruitlength = len(fruit)
    for i in range(0,int(fruitlength)):
        print(fruit[i])
        
    amount = str(input("How many items would you like to buy (Type in a number between 1 and 8!): "))
    length_input1 = len(amount)
    info = list(amount)
    for i in range(0,length_input1):
        checkinput = ord(str(info[i]))
        if (checkinput < 49 or checkinput > 56):
            print("Type in a correct input")
            getinfo()
        Getitems()
        
def Getitems():
    global items,temporary
    items = [ ]
    for i in range(0,int(amount)):
        whichone = str(input("Which Item would you like to add to cart (Type a number from 1 - 8): "))
        length = len(whichone)
        check1 = list(whichone)
        for i in range(0,int(length)):
            checkinput1 = ord(str(check1[i]))
            if(checkinput1 < 49 or checkinput1 > 56):
                print("Type in a correct input")
                Getitems()
            items.append(whichone)
    temporary = items
    info2()
    
def info2():
    for i in range(0,int(amount)):
        howmuch = str(input("How many pounds of item " + temporary[i] + " would you like to buy: "))
        length = len(howmuch)
        check2 = list(howmuch)
        for i in range(0,int(length)):
            checkinput2 = ord(str(check2[i]))
            if(checkinput2 < 48 or checkinput2 > 57):
                print("Type in a correct input")
                info2()
            pounds.append(howmuch)
    print(pounds)
    print(items)
            
def main():
    getinfo()

if __name__ == "__main__":
    main()
