import pandas as pd

file_path = "../Resources/budget_data.csv"
budget_data_df = pd.read_csv(file_path, encoding="utf-8")

#budget_data_df.head()

count_months =  budget_data_df["Date"].count()

total_profit = budget_data_df["Profit/Losses"].sum()


#get date of maximum profit
max_record = budget_data_df["Profit/Losses"].max()

for index, row in budget_data_df.iterrows():
    #print (row["Date"], row["Profit/Losses"])
    if(row["Profit/Losses"]) == max_record:
        max_id = row["Date"]

#get date of minimum profit/greatest loss
min_record = budget_data_df["Profit/Losses"].min()

for index, row in budget_data_df.iterrows():
    if(row["Profit/Losses"]) == min_record:
        min_id = row["Date"]



print("Financial Analysis")
print("-------------------------")
print(f'Total Months: {count_months}')
print(f'Total: ${total_profit}')
print(f'Greatest Increase in Profits: {max_id} (${max_record})')
print(f'Greatest Decrease in Profits: {min_id} (${min_record})')
