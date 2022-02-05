import prettytable
import mysql.connector
import os
import csv
con_Str = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@1234",
    database="project"
    )
cursor = con_Str.cursor()
# Option 1 fuction call
def option1():
    try:
        file = open("bill.csv","a",newline="")
        writer = csv.writer(file)
        headerlist = ["Item ID","Item Name","Price/Item","Quantity","Total Price"]
        writer.writerow(headerlist)
        amount = 0
        while True:
            l1 = []
            query1 = "select * from items where item_id = %s;"
            item_id = input("Enter the item id : ")
            cursor.execute(query1,[item_id])
            result = cursor.fetchall()
            for i in result:
                table = prettytable.PrettyTable(["Item ID","Item Name","Price per Item"])    
                table.add_row(i)
                print("\n\t   Item Description")            
                print(table,"\n")
                l2 = []
                l2 = list(i)
                l1.extend(l2)
                price = l1[2]
                quantity = int(input("Enter the quantity of item : "))
                l1.append(quantity)
                total = price * quantity
                l1.append(total)
                amount += total
                writer.writerow(l1)
            ch = input("Do yo want to purchase more items y/n : ")
            if ch in ["y","n"]:    
                if ch == "n":
                    break
            else:
                print("Wrong input !! try again")
        writer.writerow(["","","","Amount to be paid",amount])
        file.close()
        os.system("cls")
        print("\n\t\t\t\tBill\n")
        file = open("bill.csv")
        table = prettytable.from_csv(file)
        print(table)
        file.close()
        os.remove("bill.csv")
        print()
    except:
        print("error 1")
        os.remove("bill.csv")
# Option 2 fuction call
def option2():
    try:
        query = "select * from items;"
        cursor.execute(query)
        result = cursor.fetchall()
        table = prettytable.PrettyTable(["Item ID","Item Name","Price per Item"])
        for i in result:    
            table.add_row(i)
        print(table)
    except:
        print("error 2")
# Option 3 fuction call
def option3():
    try:
        with open("project.csv","a",newline = "") as file:
            writer = csv.writer(file)
            while True:
                l1 = []
                a = int(input("Enter the item id : "))
                b = input("Enter the item name : ")
                c = int(input("Enter the item price : "))
                l1.append(a)
                l1.append(b)
                l1.append(c)
                writer.writerow(l1)
                ch = input("Do yo want to add more items y/n : ")
                if ch in ["y","n"]:    
                    if ch == "n":
                        break
                else:
                    print("Wrong input !! try again")
        with open("project.csv") as file:
            reader = csv.reader(file)
            for i in reader:
                query = "insert into items values(%s,%s,%s);"
                cursor.execute(query,i)
                con_Str.commit()
            print("Record Added succesfully")
        os.remove("project.csv")
    except:
        print("error 3")
        os.remove("project.csv")
# Option 4 fuction call
def option4():
    try:
        while True:
            query = "delete from items where item_id = %s;"
            item_id = input("Enter the item id to be deleted : ")
            cursor.execute(query,[item_id])
            con_Str.commit()
            print("Record Removed succesfully")
            ch = input("Do yo want to remove more items y/n : ")
            if ch in ["y","n"]:    
                if ch == "n":
                    break
            else:
                print("Wrong input !! try again")
    except:
        print("error 4")
# Main Block Program Starts
def main_menu():
    try:
        while True:
            os.system("cls")
            print("\t\t\t Billing System\n")
            print("\t\t 1.Generate Bill")
            print("\t\t 2.Show List of Items")
            print("\t\t 3.Add Item")
            print("\t\t 4.Remove Item")
            print("\t\t 5.Exit\n")
            opt = int(input("Enter the Option : "))
            if opt == 1:
                option1()
            elif opt == 2:
                option2()
            elif opt == 3:
                option3()
            elif opt == 4:
                option4()
            elif opt == 5:
                break
            else:
                print("Wrong Input try again")
            ch = input("Do You want to continue to main menu y/n : ")
            if ch in ["y","n"]:    
                if ch == "n":
                    break
            else:
                print("Wrong input !! try again")
    except:
        print("error 0")
# Main Block Program Call
main_menu()