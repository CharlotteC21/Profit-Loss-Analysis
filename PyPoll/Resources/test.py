import os
import csv

file = os.path.join("Resources", "election_data.csv")

C1 = "Khan"
C2 = "Correy"
C3 = "Li"
C4 = "O' Tooley"
C1votes = 0 
C2votes = 0
C3votes = 0
C4votes = 0

total_votes = 0
candidates = 0
candidate_list = []
testdict = {}

with open (file) as location:
    Blueberries = csv.reader(location, delimiter = ",")
    csv_header = next(Blueberries)
    for row in Blueberries:

        total_votes = total_votes + 1
        currentC = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            testdict[candidate_name]

        for name in candidate_list:
            testdict[name] = eval

        if currentC == C1:
            C1votes = C1votes + 1
        elif currentC == C2:
            C2votes = C2votes + 1
        elif currentC == C3votes:
            C3votes = C3votes + 1 
        else:
            C4votes = C4votes + 1

C1per = round((C1votes/total_votes) * 100, 3)
C2per = round((C2votes/total_votes) * 100, 3)
C3per = round((C3votes/total_votes) * 100, 3)
C4per = round((C4votes/total_votes) * 100, 3)

if C1votes >= C2votes and C1votes >= C3votes and C1votes >= C4votes:
    winner = C1
elif C2votes >= C1votes and C2votes >= C3votes and C2votes>= C4votes:
    winner = C2
elif C3votes >= C1votes and C3votes >= C2votes and C3votes >= C4votes:
    winner = C3
else:
    winner = C4

print("Election Results")
print("------------")
print(f"Total Votes: {total_votes}")
print("-------------")
print(f"{C1}: {C1per}% ({C1votes})")
print(f"{C2}: {C2per}% ({C2votes})")
print(f"{C3}: {C3per}% ({C3votes})")
print(f"{C4}: {C4per}% ({C4votes})")
print("-------------")
print(f"Winner: {winner}")
print("-------------")

outpath = os.path.join("analysis", "PyPoll_output.txt")

with open(outpath, "w") as file:
    file.write (f"Election Results")