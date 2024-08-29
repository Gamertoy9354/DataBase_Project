import pandas as pd
path = ""
print("Welcome to the database. please sign in to use the DataBase and first register will be ADMIN: ")
def is_excel_file_empty(file_path):
    # Read the Excel file
    excel_data = pd.ExcelFile(file_path, engine = "openpyxl")
    # Check each sheet for content
    for sheet_name in excel_data.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine = "openpyxl")
        if not df.empty:
            return False  # The file is not empty
    return True  # The file is empty
file_path = path
if is_excel_file_empty(file_path):
    priority = "ADMIN"
else:
    priority = "USER"
username = input("Please Enter your username it should not have any space and more than 3 letters: ")
ul = len(username)
if ul > 3:
    DOB = input("Please Enter your Date Of Birth in DD/MM/YY format: ")
    firstN = str(input("Please Enter your first name as per your documents: "))
    midN = str(input("Please enter your middle name, if you dont have type 'null': "))
    lastN = str(input("Enter your last name as per your documents: "))
    phoneno = int(input("Enter your phone no without country code: "))
    plen = len(str(phoneno))
    if plen == 10:
        print("now Enter your password it should me longer than 5 char it should have atleast one upper case letter and a numeric value: ")
        password = input("Enter the password: ")
        passs = str(password)
        passlen = len(passs)
        passwordRR = input("Please Enter your password again to confirm: ")
        passr = str(passwordRR)
        passrlen = len(passr)
        if passlen > 5 and any(char.isupper() for char in passs) and any(char2.isdigit() for char2 in passs) and passs == passr:
            #making the passwords and username dataframe
            #making the DataFrame
            dataf = pd.DataFrame({"username":username,"Priority":priority,"first name":firstN,"middle Name":midN,"Last Name":lastN,"Date Of Birth":DOB,"Phone No.":phoneno,"password":passs},index=[1])
            #reading the old excel sheet
            edf = pd.read_excel(path,engine="openpyxl")
            #making changes to the DataFrame
            cdf = pd.concat([edf,dataf],ignore_index=True)
            #making changes to the Excel Sheet
            cdf.to_excel(path ,index = False , engine = "openpyxl")
            print("Great your account has been created!")
            exit()
        else:
            print("your password didn't match with our requirments please try again!")
            exit()
    else:
        print("Please enter a valid phone no.")
        exit()
else:
    print("please try again your information was incorrect")
    exit()