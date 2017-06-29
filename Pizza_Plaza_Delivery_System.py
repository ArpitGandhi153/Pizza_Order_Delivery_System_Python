#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import getpass
import sys

class UserDetails:
    uName = ""
    uPass = ""

    def __init__(self,uName,uPass):
        self.uName = uName
        self.uPass = uPass

# Beverages Selection
def beveragesInput():
    with open("BeveragesList.csv", "r") as file:
        beverages = file.readlines()

        for item in range(len(beverages)):
            print "\t[", item + 1, "] " + beverages[item].split(",")[0] + "  ₹" + beverages[item].split(",")[1]
        add = '1'
        while add == '1':
            itm = raw_input("Your Beverge : ")
            beverageList.append(beverages[int(itm) - 1])
            add = raw_input("Want to add more Beverage? [1] yes [2] No : ")

# Starters Selection
def startesInput():
    with open("StartersList.csv", "r") as file:
        starters = file.readlines()
        for item in range(len(starters)):
            print "\t[", item + 1, "] " + starters[item].split(",")[0] + "  ₹" + starters[item].split(",")[1]
        add = '1'
        while add == '1':
            itm = raw_input("Your Starter : ")
            starterList.append(starters[int(itm) - 1])
            add = raw_input("Want to add more Starter? [1] yes [2] No : ")

# Pizzas Selection
def pizzaInput():
    with open("PizzaList.csv", "r") as file:
        pizza = file.readlines()
        for item in range(len(pizza)):
            print "\t[", item + 1, "] " + pizza[item].split(",")[0] + "  ₹" + pizza[item].split(",")[1]
        add = '1'
        while add == '1':
            itm = raw_input("Your Pizza : ")
            pizzaList.append(pizza[int(itm) - 1])
            add = raw_input("Want to add more Pizza? [1] yes [2] No : ")

# Deserts Selection
def dessertInput():
    with open("DessertList.csv", "r") as file:
        desserts = file.readlines()
        for item in range(len(desserts)):
            print "\t[", item + 1, "] " + desserts[item].split(",")[0] + "  ₹" + desserts[item].split(",")[1]
        add = '1'
        while add == '1':
            itm = raw_input("Your Dessert : ")
            dessertList.append(desserts[int(itm) - 1])
            add = raw_input("Want to add more Dessert? [1] yes [2] No : ")

# View Selected Items
def viewOrder(beverageList, starterList, pizzaList, dessertList):
    totalPrice = 0
    print "\n======================================"
    print "\t\tYour Order"
    print "======================================"
    bItems = []
    sItems = []
    pItems = []
    dItems = []
    if beverageList != []:
        print "*\n* Beverages : "
        for item in beverageList:
            print "*\t" + str(item).split(",")[0]
            bItems.append(str(item).split(",")[0])
            totalPrice += int(str(item).split(",")[1])
    else:
        print "*\n* [No Beverages]"
    if starterList != []:
        print "*\n* Starters : "
        for item in starterList:
            print "*\t" + str(item).split(",")[0]
            sItems.append(str(item).split(",")[0])
            totalPrice += int(str(item).split(",")[1])
    else:
        print "*\n* [No Starters]"
    if pizzaList != []:
        print "*\n* Pizza : "
        for item in pizzaList:
            print "*\t" + str(item).split(",")[0]
            pItems.append(str(item).split(",")[0])
            totalPrice += int(str(item).split(",")[1])
    else:
        print "*\n* [No Pizzas]"
    if dessertList != []:
        print "*\n* Desserts : "
        for item in dessertList:
            print "*\t" + str(item).split(",")[0]
            dItems.append(str(item).split(",")[0])
            totalPrice += int(str(item).split(",")[1])
    else:
        print "*\n* [No Desserts]"
    return totalPrice, bItems, sItems, pItems, dItems

# Confirm  order and View Full Order (by calling viewOrder())
def viewAndPlaceOrder(uDetail, beverageList, starterList, pizzaList, dessertList):

    totalPrice,bItems,sItems,pItems,dItems = viewOrder(beverageList, starterList, pizzaList, dessertList)
    print "\n======================================"
    print "Total Price : \t", totalPrice, "₹"
    print "======================================"
    uCon = raw_input("Confirm Your Order? [1] Confirm [2] Cancel : ")
    if uCon == '1':
        currentDate = str(datetime.datetime.now()).split(" ")[0]
        # oDetail = OrderDetail(beverageList, starterList, pizzaList, dessertList, str(currentDate), totalPrice)
        with open(".OrderDetails.txt", "a") as file:
            file.write(str(uDetail.uName) + "/")
            file.write(str(bItems) + "/")
            file.write(str(sItems) + "/")
            file.write(str(pItems) + "/")
            file.write(str(dItems) + "/")
            file.write(str(totalPrice) + "/")
            file.write(str(currentDate) + "\n")
        print "\n*************************************"
        print "Thank You for Ordering at Pizza Plaza"
        print "Your Order Will Be Deliver in 30 min "
        print "********** Have a Good Day **********"

# Execution Starts
print "\n[1]New User"
print "[2]Existing User"
uType = raw_input("\nYour Choice : ")
flag =False
uDetail = None
if uType == '1':
    uName = raw_input("\nYour Name : ")
    uPass = getpass.getpass("Your Password : ")
    with open(".UserDetails.csv", "ab") as file:
        file.write(uName+",")
        file.write(uPass+"\n")
    if raw_input("You want to Shop with us [1] Yes [2] No : ") == '1':
        uDetail = UserDetails(uName, uPass)
        flag = True
    else:
        sys.exit()
elif uType == '2':
    uName = raw_input("\nYour Name : ")
    uPass = getpass.getpass("Your Password : ")
    with open(".UserDetails.csv", "rb") as file:
        data = file.readlines()
        for user in data:
            uData = str(user).split(",")
            if uData[0] == uName:
                if uData[1].rstrip('\n') == uPass:
                    uDetail = UserDetails(uName, uPass)
                    flag = True
                    break
if flag == True:
    print "\n[1] Place Order\n[2] View Order Details"
    uChoice = raw_input("\nYour Choice : ")
    if uChoice == '1':
        uAns = '1'
        beverageList = []
        starterList = []
        pizzaList = []
        dessertList = []
        while uAns == '1':
            print "================================="
            print "*\t[1] Beverages\t\t*\n*\t[2] Starters\t\t*\n*\t[3] Pizza\t\t*\n*\t[4] Dessert\t\t*"
            print "================================="
            uInput = raw_input("Your Choice : ")
            print "=========================================================="
            if uInput == '1':
                beveragesInput()
            elif uInput == '2':
                startesInput()
            elif uInput == '3':
                pizzaInput()
            elif uInput == '4':
                dessertInput()
            print "=========================================================="
            uAns = raw_input("Do you want to add More Stuff? [1] Yes\t[2] No : ")
        viewAndPlaceOrder(uDetail, beverageList, starterList, pizzaList, dessertList)
    elif uChoice == '2':
        with open(".OrderDetails.txt", "r") as file:
            uOrders = file.readlines()
            orderNo = 0
            for order in uOrders:
                oDetail = str(order).split("/")
                if oDetail[0] == uName:
                    orderNo += 1
                    print "\n*********************************************"
                    print "Order :\t", orderNo
                    print "*********************************************"
                    print "*\t Date :\t", oDetail[6].rstrip("\n")
                    print "*\t Beverages :\t" + oDetail[1]
                    print "*\t Starters :\t" + oDetail[2]
                    print "*\t Pizzas :\t" + oDetail[3]
                    print "*\t Desserts: \t" + oDetail[4]
                    print "*\t\n*\t Total Price :\t", oDetail[5]
            print "********************************************"
            print "Total Orders : ", orderNo
            print "********************************************"
    else:
        print "Invalid Choice"
        exit()
else:
    print "User Name or Password Invalid"