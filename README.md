# Colorado Congressional Election Analysis

## Project Overview
A Colorado Board of Elections employee has tasked us with completing an election audit of a local Congressional election. Tasks included:
- Calculate the total number of votes cast.
- Get a complete list of candidates whom received votes.
- Calculate the total number of votes recieved for each candidate.
- Calculate the percentage of votes received by each candidate.
- Determine the winner of the election by popular vote.

## Resources
Data Source: election_results.csv

Software: Python 3.10.5, Visual Studio Code 1.38.1

## Election/Audit Results

**TOTAL VOTES:** *369,711*

**VOTES BY COUNTY:**

- **Jefferson:** *10.5% (38,855)*
- **Denver:** *82.8% (306,055)*
- **Arapahoe:** *6.7% (24,801)*
- **Largest county turnout**: *Denver*

**VOTES BY CANDIDATE:**

- **Charles Casper Stockham:** *23.0% (85,213)*
- **Diana DeGette:** *73.8% (272,892)*
- **Raymon Anthony Doane:** *3.1% (11,606)*

**ELECTION RESULTS**

- **Winner:** *Diana DeGette*

- **Winning vote count:** *272,892*

- **Winning vote percentage:** *73.8%*

## Election/Audit Summary
The python script that was written to perform the audit is both accurate and versatile.  Since all of the outputs and arrays are read directly from the data file (.csv file) and not pre-defined in the code itself, it can be reapplied to any data set with minimal adjustments to the code based on column and row assignments within the future datasets. This would also require additional ``for`` loop statements to calculate any new data and additions to the ``print`` and ``write`` functions to display the additional data correctly.
! [ row code](https://github.com/Ian-T-Dixon/Election_Analysis/Resources/row_code.png)


This will save an undefinable amount of time moving forward and reduce the number of workers required to audit future elections.
