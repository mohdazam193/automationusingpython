for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]" , end="")
    print()

#Example of nested loops - to pair team matches

team = ['D ragon','Wolves','Panda', 'Unicorns']
for home_team in team:
    for away_team in team:
        if home_team != away_team:
            print("Schedule Match :" + home_team + " vs " + away_team)
