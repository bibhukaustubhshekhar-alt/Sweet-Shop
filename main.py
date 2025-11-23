import pandas as pd
import matplotlib.pyplot as plt
import random
import random

def addSweet(df):
    code = int(input("Enter the sweet code "))
    name = input("Enter the name of the sweet ")
    price = int(input("Enter cost per kg "))
    qty = float(input("Enter quantity in kgs "))
    ig = input("Enter the main ingredient ")
    df.loc[code] = [name, price, qty, ig]
    print("\nAdded Successfully \n")


print("_"*50)
print("\t\t Bholu 56 Bhog")
print("_"*50)
df = pd.read_csv("mithai.csv")
k=random.randint(1000,9999)
print("Captcha;",k)
print('enter captcha')
if(int(input())==k):
    c=True
else:
    c=False
    print("Wrong Input")


while c==True:
    print("Press 1 - Add a New Mithai")
    print("Press 2 - Show all available sweets")
    print("Press 3 - Search the sweet")
    print("Press 4 - Delete any sweet")
    print("Press 5 - Update/add sweet")
    print("Press 6 - Create Bill of customer(one sweet)")
    print("Press 7 - Show Chart of Sweets")
    print("Press 8 - Show Chart of Bills")
    print("Press 9 - Exit or Quit")
    a  = int(input("Enter your choice : "))
    if a == 1:
        addSweet(df)
    elif a == 2:
        print("\n","*"*50)
        print(df)
        print("*"*50)
    elif a == 3:
        code = int(input("Enter the sweet code to be searched : "))
        if code in df.index:
            print(df.loc[code])
            print("\n")
        else:
            print("No sweet found with this code ")
    elif a == 4:
        code = int(input("Enter the sweet code to be deleted : "))
        if code in df.index:
            df.drop(code,inplace=True)
            print("\nDeleted\n")
        else:
            print("No sweet found with this code ")
    elif a == 5:
        code = int(input("Enter the sweet code to be updated : "))
        if code in df.index:
            name = input("Enter the updated name of the sweet ")
            price = int(input("Enter updated cost per kg "))
            qty = float(input("Enter quantity in kgs "))
            ig = input("Enter the main ingredient ")
            df.loc[code] = [name,price,qty,ig]
            print("\nUpdated\n")
        else:
            print("No sweet found with this code ")
    elif a == 6:
        print("Available Sweets ")
        print("\n", "*" * 50)
        print(df)
        print("*" * 50)
        code = int(input("Enter the code of the sweet to be purchased : "))
        if code in df.index:
            qty = int(input("Enter the quantity to be purchased : "))
            amt = qty * df.loc[code,"Cost"]
            print("Your Due Amount is ",amt)
            name = input("Enter Customer name : ")
            b_date = input("Enter Billing Date : ")
            bf = pd.read_csv("customer.csv",index_col="billid")
            bf.loc[random.randint(1000,9999)] = [name,b_date,amt,df.loc[code,"Name"]]
            bf.to_csv("customer.csv")
        else:
            print("No sweet found with this code ")
    elif a == 7:
        plt.bar(df["Name"],df["Cost"],color="red")
        plt.title("Rate List of Sweets")
        plt.show()
    elif a == 8:
        m = pd.read_csv("customer.csv")
        plt.title("Total Sweets Sold")
        plt.bar(m["name"],m["order_amt"],color="orange")
        plt.show()
    elif a == 9:
        df.to_csv("mithai.csv",index=False)
        print("Thanks for Visiting")
        print("Waiting for your next visit")
        print("\tData Updated !!!")
        break