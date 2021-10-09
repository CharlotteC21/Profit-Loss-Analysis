import os
import csv
# from statistics import mean

file = os.path.join("Resources", "budget_data.csv")

totalpl = 0
Months = 0
profits = []

with open("budget_data.csv") as csvfile:
    PyBankData = csv.reader(csvfile, delimiter = ',')

    first_row = next(PyBankData)
    starting_row = next(PyBankData)

    Months += 1

    greatestinc = int(starting_row[1])
    greatestinc_date = starting_row[0]
    greatestdec = 0
    greatestdec_date = None

    for row in PyBankData:

        Months += 1
        
        current_profits = int(row[1])
        current_date = row[0]

        profits.append(current_profits)

        totalpl += current_profits

        if (current_profits > greatestinc):
            greatestinc = current_profits
            greatestinc_date = current_date
        elif (current_profits < greatestdec):
            greatestdec = current_profits
            greatestdec_date = current_date

    print("-------------------------------------------")
    print("Financial Analysis")
    print("Months: ", Months)
    print("Total: $", totalpl)
    print("Average Change: $", round(mean(profits),2))
    print("Greatest Increase in Profit is: ", greatestinc_date, " $", greatestinc)
    print("Greatest Decrease in Profit is: ", greatestdec_date, " $",greatestdec)

    #export txt file w/ results
    outpath = os.path.join("analysis", "PyBank_output.txt")

    with open(outpath, "w") as file:
        file.write (f"PyBank Results")  