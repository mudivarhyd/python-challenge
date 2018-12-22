# Modules to import
import os
import csv

# Declare variables
monthcount = 0
totalamount = 0
budgetList = []
#monthlyProfitChange = []
profitchange = []


# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Open the CSV budget file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #To move to second line (avoid header line)
    next(csvreader)
    #Calculate total months
    monthcount = len(csvfile.readlines())
    #Reset the pointer to the first line in the file
    csvfile.seek(0)
    #To move to second line (avoid header line)
    next(csvreader)

    # Loop through to calculate total amount and build budget list
    for row in csvreader:
        totalamount += int(row[1])
        budgetList.append(row)
    # Build the profit/losss change list to calculate greatest increase and descrease of profit/loss
    for i in range(monthcount - 1):
        profitchange.append(int(budgetList[i+1][1])-int(budgetList[i][1]))
    
    #Calculate greatest increase in profits and greatest descrease in losses
    GreatestIncreaseInProfits = max(profitchange)
    GreatestDecreaseInProfits = min(profitchange)

    #Assigning greatest increase and greatest descrease to proper month using index, use plus 1 to get next month
    MaxIncreaseMonth = budgetList[profitchange.index(max(profitchange)) + 1][0]
    MaxDecreaseMonth = budgetList[profitchange.index(min(profitchange)) + 1][0]

    #Caculate average change in profit/loss
    AverageChange = round(sum(profitchange)/len(profitchange),2 )

        #Print statements to the terminal
    print("Financial Analysis")
    print("------------------------------------------------------")
    print(f"Total Months:    {monthcount}")
    print(f"Total Amount:   ${totalamount}")
    print(f"Average Change: ${AverageChange}")
    print(f"Greatest Increase in Profits: {MaxIncreaseMonth} (${GreatestIncreaseInProfits})")
    print(f"Greatest Decrease in Profits: {MaxDecreaseMonth} (${GreatestDecreaseInProfits})")

    #Write to output file
    output_file = os.path.join("Financial_Analysis.txt")
    with open(output_file, "w") as file:

    #Write what is printed on terminal to Financial_Analysis.txt
        file.write("Financial Analysis")
        file.write("\n")
        file.write("------------------------------------------------------")
        file.write("\n")
        file.write(f"Total Months:    {monthcount}")
        file.write("\n")
        file.write(f"Total Amount:   ${totalamount}")
        file.write("\n")
        file.write(f"Average Change: ${AverageChange}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {MaxIncreaseMonth} (${GreatestIncreaseInProfits})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {MaxDecreaseMonth} (${GreatestDecreaseInProfits})")
