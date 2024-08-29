import pandas as pd     
def createfunc():
    directory = str(input("Please Enter your Directory To Save: "))
    filename1 = str(input("Please Enter Your File Name: "))
    filename = filename1+".xlsx"
    head = []
    items_dict = {}
    ranger = int(input("Please enter the amount of entries you want: "))
    for i in range(ranger):
        print("Your", str(i + 1), "Heading: ")
        heading = input().strip()
        head.append(heading)
        print("How many items do you want for heading", heading + "?: ")
        itemranger = int(input())
        item_list = []
        for z in range(itemranger):
            print("Your", str(z + 1), "item for heading",heading,":")
            iteming = input().strip()
            item_list.append(iteming)
        items_dict[heading] = item_list
    df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in items_dict.items()]))
    print(df)
    chose = str(input("Do you want to create the exel file with this dataframe?: "))
    if chose == "yes" or "Yes":
        filepath = f"{directory}/{filename}"
        df.to_excel(filepath ,index = False , engine = "openpyxl")
