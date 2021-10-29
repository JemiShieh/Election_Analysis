# Data to retrieve/calculate
# 1. Total number votes cast
# 2. Complete list of candidates receiving votes
# 3. Percentage votes won by each candidate
# 4. Total number votes won by each candidate
# 5. Winner of election based on popular vote

# Add dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)