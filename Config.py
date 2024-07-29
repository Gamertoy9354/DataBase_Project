import pandas as pd
path = "/home/shis/Desktop/desktop folders/python project/DATABASE/ADMINCABIN/Users.xlsx"
edf = pd.read_excel(path,engine="openpyxl")
Ulist = []
print("Welcome to ADMIN Panel")
username = input("Enter your username: ")
uedf = edf["username"]
print(uedf)
for i in uedf:
    Ulist.append(i)
# Check if the username exists in the DataFrame
if username in edf['username'].values:
    # Locate the row where the username matches
    user_row = edf[edf['username'] == username]
    
    # Access the 'password' column for this row
    password = user_row['password'].values[0]  # Use [0] to get the actual value
    priority = user_row["Priority"].values[0]
    firstname = user_row["first name"].values[0]
    upassword = input("Please enter your password: ")
    if upassword == password:
        if priority == "ADMIN":
            print(f"welcome back {firstname} your current status is ADMIN")
            print("type 'help' to list out all commands available")
            cmd = input("Enter your command: ")
            if cmd == "help":
                print("type 'CHANGEPRIO' to change the priotrity of a user\n type 'LISTU' to list all the users in the database: ")
                cmd = input("Enter your command: ")
                if cmd == "CHANGEPRIO":
                    cuser = input("Enter the username of the user you want to change the priority of: ")
                    if cuser in Ulist:
                        cuser_row = edf[edf['username'] == cuser]
                        cfirstname = cuser_row["first name"].values[0]
                        Nprior = input(f"Enter new priority of {cfirstname} :  ")
                        if Nprior == "ADMIN" or "USER" or "EMP":
                            print("priority has been changed (need to do work its incomplete!!!!!)")
                    else:
                        print(f"{cuser} is not present in the database.")
                        exit()
        else:
            print(f"{firstname} You do not have access to config you are an {priority}")
    else:
        print(f"{firstname} Your password does not match to your username")
else:
    print("Your username is not in the database")
    exit()