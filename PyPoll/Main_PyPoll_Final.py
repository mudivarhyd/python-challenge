# Modules to import
import os
import csv

# Declare variables
totalvotes = 0
khanvotes = 0
correyvotes = 0
livotes = 0
otooleyvotes = 0

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

# Open the CSV election file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #To move to second line (avoid header line)
    next(csvreader)
    #Calculate total votes
    totalvotes = len(csvfile.readlines())
    #Reset the pointer to the first line in the file
    csvfile.seek(0)
    #To move to second line (avoid header line)
    next(csvreader)

# Loop through to calculate totals for each candidate
    for row in csvreader:
        # For each candidate found calculate the total votes for that candate
        if row[2] == "Khan":
            khanvotes += 1
        elif row[2] == "Correy":
            correyvotes += 1
        elif row[2] == "Li":
            livotes += 1
        elif row[2] == "O'Tooley":
            otooleyvotes += 1

# Percentage of Votes each candidate won.
khanpercentage = (khanvotes/totalvotes) * 100
correypercentage = (correyvotes/totalvotes) * 100
lipercentage = (livotes/totalvotes) * 100
otoolpercentage = (otooleyvotes/totalvotes) * 100

# Find out the winner by max total votes
# List for candidate total votes
candidatevoteslist = [khanvotes, correyvotes,livotes,otooleyvotes]
# Find out max from the list above
winnervotes = max(candidatevoteslist)
# Find out who is the winner by total votes
if winnervotes == correyvotes:
    winner = "Correy"
elif winnervotes == livotes:
    winner = "Li"
elif winnervotes == otooleyvotes:
    winner = "O' Tooley"
elif winnervotes == khanvotes:
    winner = "Khan"

#print(f"Winner: {winner}")
#print(f"List: {max(candidatevoteslist)}")

#Print statements to the terminal
print("Election Results")
print("------------------------------------------------------")
print(f"Total Votes: {totalvotes}")
print("------------------------------------------------------")
print(f"Khan:        {khanpercentage: .3f}% ({khanvotes})")
print(f"Correy:      {correypercentage: .3f}% ({correyvotes})")
print(f"Li:          {lipercentage: .3f}% ({livotes})")
print(f"O'Tooley:    {otoolpercentage: .3f}% ({otooleyvotes})")
print("------------------------------------------------------")
print(f"Winner:       {winner}")
print("------------------------------------------------------")

#Write to output file
output_file = os.path.join("Election_Results.txt")
with open(output_file, "w") as file:

#Write what is printed on terminal to Election_Results.txt
    file.write("Election Results")
    file.write("\n")
    file.write("--------------------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {totalvotes}")
    file.write("\n")
    file.write("--------------------------------------------")
    file.write("\n")
    file.write(f"Khan:     {khanpercentage: .3f}% ({khanvotes})")
    file.write("\n")
    file.write(f"Correy:   {correypercentage: .3f}% ({correyvotes})")
    file.write("\n")
    file.write(f"Li:       {lipercentage: .3f}% ({livotes})")
    file.write("\n")
    file.write(f"O'Tooley: {otoolpercentage: .3f}% ({otooleyvotes})")
    file.write("\n")
    file.write("----------------------------------------------")
    file.write("\n")
    file.write(f"Winner:    {winner}")
    file.write("\n")
    file.write("----------------------------------------------")

