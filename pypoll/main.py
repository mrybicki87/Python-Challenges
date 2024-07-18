import os
import csv

election_data_csv= os.path.join('..', 'resources', 'election_data.csv')

with open(election_data_csv, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(f"CSV Header: {csv_header}")

    charles_count = 0
    diana_count = 0
    raymon_count = 0
    total_votes = 0 

    for row in csvreader:
        total_votes += 1 # adds 1 to total_votes for each row
        for column in row:  # if statements will add one to each candidates vote count per row that they appear in

            if column == "Charles Casper Stockham":
                charles_count += 1
            elif column == "Diana DeGette":
                diana_count += 1
            elif column == "Raymon Anthony Doane":
                raymon_count += 1
        


charles_percent = (float(charles_count)/float(total_votes))*100  # percent equals each candidates vote count / total votes * 100
diana_percent = (float(diana_count)/float(total_votes))*100
raymon_percent = (float(raymon_count)/float(total_votes))*100

if charles_count > diana_count and charles_count > raymon_count:  # compare the number of votes to see which candidate has more votes than their competition
    winner = "Charles Casper Stockham"
elif diana_count > charles_count and diana_count > raymon_count:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"


analysis_txt = os.path.join('..', 'analysis', 'pypoll.txt')

with open(analysis_txt, "a") as f:
    print("Election Results", file=f)
    print("------------------------------", file=f)
    print("Total Votes: " + str(total_votes), file =f)
    print("------------------------------", file=f)
    print("Charles Casper Stockham: " + str(round(charles_percent, 3)) + "% " + "("+str(charles_count)+")", file = f)
    print("Diana DeGette: " + str(round(diana_percent, 3)) + "% " + "("+str(diana_count)+")", file = f)
    print("Raymon Anthony Doane: " + str(round(raymon_percent, 3)) + "% " + "("+str(raymon_count)+")", file = f)
    print("------------------------------", file = f)
    print("Winner: " + winner, file = f)

