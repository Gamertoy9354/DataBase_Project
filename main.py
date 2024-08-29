import pandas as pd
path = ""
edf = pd.read_excel(path,engine="openpyxl")
username = input("Enter your username: ")
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
        if priority == "EMP":
            print(f"welcome back {firstname} your current status is employee")
        elif priority == "USER":
            print(f"welcome back {firstname} your current status is USER")
        elif priority == "ADMIN":
            print(f"welcome back {firstname} your current status is ADMIN")
        else:
            print("you do not have access to the DataBase")
else:
    print("Username not found.")
