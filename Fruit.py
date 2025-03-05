import os.path
from os import path
def getinfo():
    global fruit,items,prices,amount
    fruit = "1. Apples $3.00/lb \n2. Banana $2.50/lb \n3. Peaches $3.50/lb\n4. Oranges $3.00/lb\n5. Mangos $4.00/lb\n6. Pears $5.00 /lb\n7. Guava $3.00 /lb \n8. Kiwi $2.50 /lb"
    items = [ ]
    prices = [ ] 
    print("FRUIT DEPARTMENT: ")
    print(fruit)

    amount = str(input("How many items would you like to buy (Type in a number between 1 and 8!): "))
    length_input1 = len(amount)
    info = list(amount)
    print(info)
    for i in range(0,length_input1):
        checkinput = ord(str(info[i]))
        if (checkinput < 49 or checkinput > 56):
            print("Type in a correct input")
            getinfo()
        Getitems()
        
def Getitems():
    counter = int(amount)
    for i in range(0,int(amount)):
        print(fruit)
        whichone = str(input("Which Item would you like to add to cart (Type a number from 1 - 8): "))
        length = len(whichone)
        list1 = list(whichone)
        for i in range(0,length):
            check = ord(list1[i])
            if (check < 49 or check > 56):
                print("Type in a correct input")
                Getitems()
        items.append(whichone)
           
def main():
    getinfo()

if __name__ == "__main__":
    main()
