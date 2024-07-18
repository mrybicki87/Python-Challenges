import os
import csv

budget_data_csv= os.path.join('..', 'resources', 'budget_data.csv')

#print(budget_data_csv)

with open(budget_data_csv, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(f"CSV Header: {csv_header}")
    
    row_count = 0
    total = 0
    total3 = 0
    greatest = 0
    least = 0
    average_total = 0
    month_greatest = 0
    month_least = 0
    for row in csvreader:
        row_count +=1  # row_count to count the number of rows in the budget csv
        total2 = 0
        try:
            total2 = int(row[1])  # try to convert the variable total2 to integer, if it cannot (for the header) the variable will go to else and be 0
            total4 = total2 - total3 # total2 is the current row, and total3 will save afterwards to be the previous rows total.  Total4 is the difference between them to track change between the rows
            if total4 == (int(row[1])):  # to cancel out the lack of change for the first row
                total4 = 0
            total3 = int(row[1])
            if total4 > greatest:  # total4 will save to greatest if it is greater than the perviously saved greatest total
                greatest = total4
                month_greatest = str(row[0])
            if total4 < least:
                least = total4 #total 4 will save to least if it is less than the previously saved least total
                month_least = str(row[0])
        except ValueError:
                total2 = 0
                average_total = 0
                
        average_total += total4        # add the totals of the changes between rows, total4, to figure out the average later
        total += total2  # add total2 to total

average_change = average_total / (row_count - 1) # the average change is the average total divided by the row count - 1 (there is no change for the first row)

analysis_txt = os.path.join('..', 'analysis', 'pybank.txt')

with open(analysis_txt, "a") as f:

    print("Financial Analysis", file = f) 
    print("-----------------------------------", file = f)       
    print("Total Months: " + str(row_count), file = f)
    print("Total: $" + str(total), file = f)
    print("Average Change: $" + str(round(average_change, 2)), file = f)
    print("Greatest Increase in Profits: " + month_greatest + " $" + str(greatest), file = f)
    print("Greatest Decrease in Profits: " + month_least + " $" + str(least), file = f)
