#-------------------------------------------------------------------------------------------------------------------------------------------------------
# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  # The total number of votes cast

  # A complete list of candidates who received votes

  # The percentage of votes each candidate won

  # The total number of votes each candidate won

  # The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

  #```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#------------------------------------------------------------------------------------------------------------------------------------------------------
# Begin actual code


# Module for setting filepaths in all operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')



# Open the file
with open(csvpath, mode='r', newline='') as csvfile:
    # Read the content
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

# --------------------------------------------------------------------------------------------------
# Loop through the CSV and check each row's candidate to calculate their votes

    # Initialize candidates' vote counts
    countKhan = 0
    countCorrey = 0
    countLi = 0
    countOTooley = 0

    # User notification
    print(f"Calculating election results.  Please wait. \n \n")
    # Loop through each row

    names = ['khan', 'correy', 'li', 'o\'tooley']
    for row in csvreader:
        # Check which candidate this row represents, then add their vote
        if row[2].lower() == 'khan':
            countKhan += 1

        if row[2].lower() == 'correy':
            countCorrey += 1

        if row[2].lower() == 'li':
            countLi += 1

        if row[2].lower() == 'o\'tooley':
            countOTooley += 1

    # Calculate total number of Votes
    totalVotes = countKhan+countCorrey+countLi+countOTooley


    # Calculate vote percentages
    percentageKhan = round((countKhan/totalVotes), 3)
    percentageCorrey = round(countCorrey/totalVotes, 3)
    percentageLi = round(countLi/totalVotes, 3)
    percentageOTooley = round(countOTooley/totalVotes, 3)

    # Find the winner
    if (countKhan > countCorrey) and (countKhan > countLi) and (countKhan > countOTooley):
        winner = "Khan"
    elif (countCorrey > countKhan) and (countCorrey > countLi) and (countCorrey > countOTooley):
        winner = "Correy"
    elif (countLi > countKhan) and (countLi > countCorrey) and (countLi > countOTooley):
        winner = "Li"
    else:
        #(countOTooley > countKhan) and (countOTooley > countCorrey) and (countOTooley > countLi):
        winner = "O'Tooley"

    print(f"Election Results \n ---------------------- \n Total Votes: {totalVotes} \n ---------------------- \n Khan: {percentageKhan}% ({countKhan}) \n Correy: {percentageCorrey}% ({countCorrey}) \n Li: {percentageLi}% ({countLi}) \n O'Tooley: {percentageOTooley}% ({countOTooley}) \n ---------------------- \n Winner: {winner} \n ----------------------")

# Write the results to a TXT file
results = open("Resources/results.txt","w+")
results.write(f"Election Results \n ---------------------- \n Total Votes: {totalVotes} \n ---------------------- \n Khan: {percentageKhan}% ({countKhan}) \n Correy: {percentageCorrey}% ({countCorrey}) \n Li: {percentageLi}% ({countLi}) \n O'Tooley: {percentageOTooley}% ({countOTooley}) \n ---------------------- \n Winner: {winner} \n ----------------------")
