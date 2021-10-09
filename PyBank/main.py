#import data
import os
import csv

#linking file to csv
file = os.path.join("Resources", "budget_data.csv")

#Variables (pl = profit/losses)
date =[]
totalpl = 0
Months = 1
greatestinc = 0
greatestdec = 0

with open (file) as csvfile:
    PyBankData = csv.reader(csvfile, delimiter = ',')

    header = next(PyBankData)
    starting_row = next(PyBankData)

    greatestinc = int(starting_row[1])
    greatestinc_date = header[0]
        
    for row in PyBankData:
        Months += 1
        totalpl += int(row[1])

        if int(row[1]) > greatestinc:
            greatestinc = int(row[1])
            greatestinc_date = row[0]
        
        if int(row[1]) < greatestdec:
            greatestdec = int(row[1])
            greatestdec_date = row[0]

            avg_change = round(totalpl/Months)

#output
    print("----------------------------------------------------")
    print ("Financial Analysis")
    print("----------------------------------------------------")
    print("Months:", Months)
    print(f'Total: ${totalpl}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profit is: {greatestinc_date} ${greatestinc}')
    print(f'Greatest Decrease in Profit is: {greatestdec_date} ${greatestdec}')
    print("----------------------------------------------------")

#export txt file w/ results
outpath = os.path.join("analysis", "PyBank_output.txt")

with open(outpath, "w") as file:
    file.write (f"PyBank Results:\n")
    file.write("----------------------------------------------------\n")
    file.write("Financial Analysis\n")
    file.write("----------------------------------------------------\n")
    file.write(f'Months:, {Months}\n')
    file.write(f'Total: ${totalpl}\n')
    file.write(f'Average Change: ${avg_change}\n')
    file.write(f'Greatest Increase in Profit is: {greatestinc_date} ${greatestinc}\n')
    file.write(f'Greatest Decrease in Profit is: {greatestdec_date} ${greatestdec}\n')
    file.write("----------------------------------------------------")
