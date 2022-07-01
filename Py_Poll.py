# The data we need to retrieve
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

#Add Dependencies
from ast import If
import csv

import os

# Assign a variable for the file to load and the path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter

total_votes = 0

# Declare candidates

candidate_options = []

# Declare candidate votes

candidate_votes = {}

# Winning Candidate and Winning Count Tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# Open the election results

with open(file_to_load) as election_data:
    
    # Read the file object with the reader function
    
    file_reader = csv.reader(election_data)
    
    #read the header row.
     
    headers = next(file_reader)
    
    #Print each roww in the CSV file
    
    for row in file_reader:
        
        # Add to the total vote count
        
        total_votes += 1
        
        # Print the candidate name from each row
        
        candidate_name = row[2]
        
        #If canidate does not match existing canidate
        
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates.
            
            candidate_options.append(candidate_name)
            
            # Begin tracking candidate votes
            
            candidate_votes[candidate_name] = 0
            
            # Increase the candidate votes by 1
            
        candidate_votes[candidate_name] += 1
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    
# 1. Iterate through the candidate list.

for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    
    votes = candidate_votes[candidate_name]
    
    # 3. Calculate the percentage of votes.
    
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # 4. Print the candidate name and percentage of votes.
    
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
    # Determine winning vote count and candidate
    
    # Determine if the votes are greater than the winning count.

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        
     # 2. If true then set winning_count = votes and winning_percent =
     
     # vote_percentage.
     
        winning_count = votes
        
        winning_percentage = vote_percentage
        
     # 3. Set the winning_candidate equal to the candidate's name.
     
        winning_candidate = candidate_name
        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)