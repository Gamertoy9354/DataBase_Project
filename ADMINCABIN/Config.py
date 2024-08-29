import pandas as pd
path = ""
Fpath = ""
edf = pd.read_excel(path,engine="openpyxl")
FFbdf = pd.read_excel(Fpath,engine="openpyxl")
Ulist = []
print("Welcome to ADMIN Panel")
username = input("Enter your username: ")
uedf = edf["username"]
flist = ["CHANGEPASS","CHANGEPRIO","LISTU","LISTFU","FIRE"]
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
    midN = user_row["middle Name"].values[0]
    lastN = user_row["Last Name"].values[0]
    DOB = user_row["Date Of Birth"].values[0]
    phoneno = user_row["Phone No."].values[0]
    upassword = input("Please enter your password: ")
    if upassword == password:
        if priority == "ADMIN":
            print(f"welcome back {firstname} your current status is ADMIN")
            print("type 'help' to list out all commands available")
            cmd = input("Enter your command: ")
            if cmd == "help":
                print("type 'CHANGEPRIO' to change the priotrity of a user\n type 'LISTU' to list all the users in the database\n Type 'FIRE' ro fire anyone from the database\n Type 'LISTFU' to list all fired users from the database:  ")
                cmd = input("Enter your command: ")
            if cmd not in flist:
                print(f"there is no command as {cmd}")
                cmd = input("enter the command or type 'help' to list all command: ")

            if cmd == "CHANGEPRIO":
                cuser = input("Enter the username of the user you want to change the priority of: ")
                if cuser in Ulist:
                    icuser_row = edf[edf['username'] == cuser].index[0]
                    cuser_row = edf[edf['username'] == cuser]
                    cfirstname = cuser_row["first name"].values[0]
                    nu = cuser_row["username"].values[0]
                    cmidN = cuser_row["middle Name"].values[0]
                    clastN = cuser_row["Last Name"].values[0]
                    cDOB = cuser_row["Date Of Birth"].values[0]
                    cphoneno = cuser_row["Phone No."].values[0]
                    cpasss = cuser_row["password"].values[0]
                    Nprior = input(f"Enter new priority of {cfirstname} :  ")
                    if Nprior in ["ADMIN","USER","EMP","FIRED"]:
                                        #making the DataFrame
                        dataf = pd.DataFrame({"username":cuser,"Priority":Nprior,"first name":cfirstname,"middle Name":cmidN,"Last Name":clastN,"Date Of Birth":cDOB,"Phone No.":cphoneno,"password":cpasss},index=[1])
                        #reading the old excel sheet
                        adf = edf.drop(icuser_row)
                        #making changes to the DataFrame
                        bdf = pd.concat([adf,dataf],ignore_index=True)
                        cdf = bdf.drop_duplicates()
                        #making changes to the Excel Sheet
                        cdf.to_excel(path ,index = False , engine = "openpyxl")
                        print(f"The Priority of {cuser} is changed to {Nprior}")
                    else:
                        print(f"there is no priority as {Nprior}")
                else:
                    print(f"{cuser} is not present in the database.")
                    exit()
            if cmd == "LISTU":
                print(edf)
            else:
                print(f"there is no command as {cmd}")
            if cmd == "FIRE":
                Fuser = input("enter the username whome you want to fire: ")
                if Fuser in edf['username'].values:
                    Fuser_row = edf[edf['username'] == Fuser].index[0]
                    Fcuser_row = edf[edf['username'] == Fuser]
                    fpassword = Fcuser_row['password'].values[0]  
                    fpriority = Fcuser_row["Priority"].values[0]
                    ffirstname = Fcuser_row["first name"].values[0]
                    fmidN = Fcuser_row["middle Name"].values[0]
                    flastN = Fcuser_row["Last Name"].values[0]
                    fDOB = Fcuser_row["Date Of Birth"].values[0]
                    fphoneno = Fcuser_row["Phone No."].values[0]
                    if fpriority != "ADMIN":
                        Fdataf = pd.DataFrame({"username":Fuser,"Priority":fpriority,"first name":ffirstname,"middle Name":fmidN,"Last Name":flastN,"Date Of Birth":fDOB,"Phone No.":fphoneno,"password":fpassword},index=[1])
                        Fdf = pd.read_excel(Fpath,engine="openpyxl")
                        Fbdf = pd.concat([Fdf,Fdataf],ignore_index=True)
                        Fbdf.to_excel(Fpath ,index = False , engine = "openpyxl")
                        Fedf = edf.drop(Fuser_row)
                        Fedf.to_excel(path ,index = False , engine = "openpyxl")
                        print(f"{Fuser} is now fired from the database! and is stored in the fired list!")
                    else:
                        print(f"you cannot FIRE {Fuser} from databse because he is an ADMIN. change his priority first.")
                else:
                    print(f"{Fuser} is not in the database!")
            if cmd not in flist:
                print(f"there is no command as {cmd}")
            if cmd == "LISTFU":
                print(FFbdf)
            if cmd not in flist:
                print(f"there is no command as {cmd}")
            if cmd == "CHANGEPASS":
                puser = input("Enter the username whose password you want to change: ")
                if puser in edf['username'].values:
                    puser_row = edf[edf['username'] == puser].index[0]
                    pcuser_row = edf[edf['username'] == puser]
                    ppassword = pcuser_row['password'].values[0]  
                    ppriority = pcuser_row["Priority"].values[0]
                    pfirstname = pcuser_row["first name"].values[0]
                    pmidN = pcuser_row["middle Name"].values[0]
                    plastN = pcuser_row["Last Name"].values[0]
                    pDOB = pcuser_row["Date Of Birth"].values[0]
                    pphoneno = pcuser_row["Phone No."].values[0]
                    print("now Enter your password it should me longer than 5 char it should have atleast one upper case letter and a numeric value: ")
                    NPA = input("Enter the password: ")
                    passs = str(NPA)
                    passlen = len(passs)
                    passwordRR = input("Please Enter your password again to confirm: ")
                    passr = str(passwordRR)
                    passrlen = len(passr)
                    if passlen > 5 and any(char.isupper() for char in passs) and any(char2.isdigit() for char2 in passs) and passs == passr:
                        pdataf = pd.DataFrame({"username":puser,"Priority":ppriority,"first name":pfirstname,"middle Name":pmidN,"Last Name":plastN,"Date Of Birth":pDOB,"Phone No.":pphoneno,"password":NPA},index=[1])
                        pdf = edf.drop(puser_row)
                #making changes to the DataFrame
                        pbdf = pd.concat([pdf,pdataf],ignore_index=True)
                #making changes to the Excel Sheet
                        pbdf.to_excel(path ,index = False , engine = "openpyxl")
                        print(f"successfully changed password of {puser} to {NPA}.")
            if cmd not in flist:
                print(f"there is no command as {cmd}")
        else:
            print(f"{firstname} You do not have access to config, you are an {priority}")
    else:
        print(f"{firstname} Your password does not match to your username")
else:
    print("Your username is not in the database")
    exit()