# Data to retrieve/calculate
# 1. Total number votes cast
# 2. Complete list of candidates receiving votes
# 3. Percentage votes won by each candidate
# 4. Total number votes won by each candidate
# 5. Winner of election based on popular vote

# Add dependencies
import csv
import os
# Assign variable to load file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign variable to save file to path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize total vote ounter
total_votes = 0

# Declare candidate options list
candidate_options = []
# Declare candidate votes empty dictionary
candidate_votes = {}

# Initialize winning candidate, count, percentage trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read header row
    headers = next(file_reader)

     # Read each row in CSV file
    for row in file_reader:
        # Add to total vote count
        total_votes = total_votes + 1

        # Print candidate name from each row
        candidate_name = row[2]

        # If candidate name not in candidate options list
        if candidate_name not in candidate_options:
            # Add candidate name to candidate options list
            candidate_options.append(candidate_name)
            
            # Track candidate vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Save results to text file
with open(file_to_save, "w") as txt_file:

    # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save final vote count to text file
    txt_file.write(election_results)

    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Determine candidate results 
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print candidate voter count and percentage to terminal
        print(candidate_results)
        # Save candidate results to text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate
        # Determine if candidate votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning_candidate equal to candidate name
            winning_candidate = candidate_name
    # Print winning candidate results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save winning candidate results to text file
    txt_file.write(winning_candidate_summary)
