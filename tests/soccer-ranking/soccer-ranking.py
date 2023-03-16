# Define game object with input and method to determine winner/loser point allotment
class GameObj:
    def __init__(self,line) -> None:
        # split game by , and whitespace 
        self.game = line.split(", ")
        # pull teams and scores from split string by last whitespace
        self.team0 = (self.game[0].strip()).rsplit(" ", 1)[0]
        self.score0 = int((self.game[0].strip()).rsplit(" ", 1)[1])
        self.team1 = (self.game[1].strip()).rsplit(" ", 1)[0]
        self.score1 = int((self.game[1].strip()).rsplit(" ", 1)[1])
        # determine winner and store points
        if self.score0 <  self.score1:
            self.points0 = 0
            self.points1 = 3
        elif self.score0 > self.score1:
            self.points0 = 3
            self.points1 = 0
        else:  
            self.points0 = self.points1 = 1

# Read input file path from user
file_path = input("Enter path to input: ")
while not file_path:
    file_path = input("Enter path to input: ")

# Define scoreboard hashtable
scoreboard = {}

# Read input line by line
with open(file_path) as f:
    for lines in f:
        # Create game object from input line
        this_game = GameObj(lines)
        # Add to scoreboard if team doesn't exist otherwise increment team points
        if this_game.team0 in scoreboard.keys():
            scoreboard[this_game.team0] += this_game.points0
        else:
            scoreboard[this_game.team0] = this_game.points0
        if this_game.team1 in scoreboard.keys():
            scoreboard[this_game.team1] += this_game.points1
        else:
            scoreboard[this_game.team1] = this_game.points1

# Rank teams by points descending then team name acsending
sorted_scoreboard = sorted(scoreboard.items(), key=lambda x: (-x[1], x[0]))

# Create ranking list - rank is equal to index+1 or previous rank if score is tied with prior rank
ranking = [1]
for i in range(1,len(sorted_scoreboard)):
    if sorted_scoreboard[i][1] == sorted_scoreboard[i-1][1]:
        ranking.append(ranking[i-1])
    else:
        ranking.append(i+1)

# Print results to console
for i in range(len(sorted_scoreboard)):
    # Account for plurality
    if sorted_scoreboard[i][1] == 1:
        pts = "pt"
    else:
        pts = "pts"
    print(str(ranking[i]) + ". " + sorted_scoreboard[i][0] + ", " + str(sorted_scoreboard[i][1]) + " " + pts)
