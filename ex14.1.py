votes = {
    "Electronics": 0,
    "Clothing": 0,
    "Food": 0,
    "Books": 0
}

selections = ["Electronics", "Food", "Electronics", "Books", "Food", "Electronics", "Clothing"]

for selection in selections:
    if selection in votes:
        votes[selection] += 1

print("Vote Count:")
for category, count in votes.items():
    print(category, ":", count)

winner = max(votes, key=votes.get)

print("Winner:", winner)
print("Votes:", votes[winner])