# Election Audit Analysis

## Election Audit Overview
Assist Colorado Board of Elections employee, Tom, in an election audit of the tabulated results for a US Congressional precinct in Colorado.

Use Python to extract and analyze data from the election results CSV file, determine votes by county and the winner of the election, and output and save the results to an external file.

1. Calculate total number of votes cast
2. Compile complete list of candidates receiving votes
3. Calculate total number of votes received by each candidate
4. Calculate percentage of votes received by each candidate
5. Determine winner of election based on popular vote  
6. Calculate total number of votes cast in each county
7. Calculate percentage of votes cast in each county
8. Determine county with highest total number of votes

## Election Audit Resources

* Data Sources: election_results.csv
* Software: Python 3.7.6, Visual Studio Code 1.61.2

## Election Audit Results

The results of the Election Analysis are as follows:

* There were 369,711 total votes cast.

* The total number and percentage of votes by county:
  - Arapahoe 6.7% 24,801  
  - Denver 82.8% 306,055 
  - Jefferson 10.5% 38,855

* The county with the highest total number of votes:
  - Denver
  
* The candidates:
  - Diana DeGette 
  - Raymon Anthony Doane
  - Charles Casper Stockham

* The election results by candidate:  
  - Diana DeGette received 272,892 votes (73.8% of total votes)  
  - Raymon Anthony Doane received 11,606 votes (3.1% of total votes)  
  - Charles Casper Stockham received 85,213 votes (23.0% of total votes)  

* The winner of the election
  - Diana DeGette who received 272,892 votes (73.8% of total votes)  

## Election Audit Summary
This script is versatile and adaptable, with modifications, to any size election data set stored in an accessible format.

For example, the script could be modified to calculate and determine additional insights such as:
  1. The winning candidate by total number and parentage of votes in each county
  2. Potential voter fraud by detecting any duplicate Ballot IDs
  3. With zip code data included, the specific polling locations with the highest voter traffic for future planning purposes
