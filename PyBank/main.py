import os
import csv

budget_data_csv = os.path.join("C:/Users/ruby/Google Drive/CloneGitlab/RU-HOU-DATA-PT-09-2019-U-C/Homework/03-Python/Instructions/PyBank", "Resources", "budget_data.csv")

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
 
   

    # initalizing values
    months = []
    total_of_pl = []
    month_profit_change = []

    # months = 0
    # sum_of_pl = 0
    # month_profit_change = 0
    # max_profit = 0
    # min_profit = 0

    # Loop through the data
    for row in csvreader:
        months.append(row[0])
        total_of_pl.append(int(row[1]))
    
    for i in range(1, len(total_of_pl)):
        month_profit_change.append((int(total_of_pl[i]) - int(total_of_pl[i-1])))


    month_profit_average = sum(month_profit_change) / len(month_profit_change)
    
    total_months = len(months)
    final_total_of_pl = sum(total_of_pl)

    max_value_change = max(month_profit_change)
    min_value_change = min(month_profit_change)
    location_of_max = month_profit_change.index(max(month_profit_change))
    month_for_max = months[location_of_max+1]
    location_of_min = month_profit_change.index(min(month_profit_change))
    month_for_min = months[location_of_min+1]


print("Financial Ananlysis")
print("________________________")
print(f"Total Months: {total_months}")
print(f"Total: $ {str(final_total_of_pl)}")
print(f"Average Change: $ { format(month_profit_average, '.2f')}")
print(f"Greatest Increase in Profits: {month_for_max} ( {str(max_value_change)})")
print(f"Greatest Decrease in Profits: {month_for_min} ( {str(min_value_change)}) ")


# Specify the file to write to
output_path = os.path.join("C:/Users/ruby/Google Drive/bootcamp/homework/03-Python/python-challenge/", "output", "pybank.txt")

with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Financial Ananlysis"])
    csvwriter.writerow(["_______________________"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: $ {str(final_total_of_pl)}"])
   
    csvwriter.writerow([f"Average Change: $ { format(month_profit_average, '.2f')}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {month_for_max} ( {str(max_value_change)})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {month_for_min} ( {str(min_value_change)})"])