import pandas as pd
from create import createfunc
from modify import modifyfunc
from view import viewfunc
with open("username.myext","r") as fileU:
    listU = []
    for i in fileU:
        listU.append(i)
with open("password.myext","r") as fileP:
    listp = []
    for z in fileP:
        listp.append(z)
for U in listU:
    x = U
print("welcome to the database please enter your credentials to login!")
userLOG = input("Please enter your username: ")
userLOGIN = userLOG+"\n"
passLOG = input("Please enter your password: ")
passLOGIN = passLOG+"\n"
if userLOGIN in listU:
    if passLOGIN in listp:
        print("You have successfully logged in!")
    else:
        print("Your Password is not correct or you have not registered yet.")
else:
    print("Your Username is not correct or you have not registered yet.")
