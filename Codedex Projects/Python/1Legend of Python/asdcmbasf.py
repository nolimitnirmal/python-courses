players = [
{"name" : "saka", "number" : 7, "position" : "RW", "goals" : 20, "assists" : 10}, 
{"name" : "gyokores", "number" : 9, "position" : "ST", "goals" : 100, "assists" : 20}, 
{"name" : "rodrygo", "number" : 11, "position" : "LW", "goals" : 20, "assists" : 15}
]

print(players[0]["goals"])

print([player["position"] for player in players])

average_goals = sum([player["goals"] for player in players]) / len(players)

print(average_goals)











