import pandas as pd

file_path = "../Resources/election_data.csv"
election_data_df = pd.read_csv(file_path, encoding="utf-8")

#election_data_df.head()

total_votes = election_data_df["Voter ID"].count()

Summary_by_candidate = election_data_df["Candidate"].value_counts()

Khan_votes = Summary_by_candidate["Khan"]
Khan_percent = format((Khan_votes/total_votes)*100,'.3f')

Correy_votes = Summary_by_candidate["Correy"]
Correy_percent = format((Correy_votes/total_votes)*100,'.3f')

Li_votes = Summary_by_candidate["Li"]
Li_percent = format((Li_votes/total_votes)*100,'.3f')

OTooley_votes = Summary_by_candidate["O'Tooley"]
OTooley_percent = format((OTooley_votes/total_votes)*100,'.3f')

winner = Summary_by_candidate.idxmax()



print("Election Results")
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
print("Khan: " + Khan_percent + "%")
print("Correy: " + Correy_percent + "%")
print("Li: " + Li_percent + "%")
print("O'Tooley: " + OTooley_percent + "%")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
