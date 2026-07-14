# Initial Data of 3 players taken as demo structure
Cricketers = [
    {
        "name": "Virat Kohli",
        "runs": 14181,
        "wickets": 5,
        "Opponents": ["Australia","England","Pakistan"]
    },

    {
        "name": "MS Dhoni",
        "runs": 10773,
        "wickets": 1,
         "Opponents": ["Australia","England","Pakistan"]
    },

    {
        "name": "Rohit Sharma",
        "runs": 11168,
        "wickets": 9,
         "Opponents": ["Australia","England","Pakistan"]
    }
]


# Functions for each action in menu
# Adding a player
def addPlayer():
    name = input("Enter Name: ")
    runs = int(input("Enter Name: "))
    wickets = int(input("Enter Name: "))
    total_opponents = int(input("Enter Total Opponents: "))
    
    player_opponents = []
    # Input all the opponent names
    for _ in range(total_opponents):
        player_opponents.append(input(f"Enter Opponent {_ + 1} name"))
        
    cricketer = { "name" : name,
      "runs" : runs ,
      "wickets" : wickets,
      "Opponents" : player_opponents
     }   
    
    Cricketers.append(cricketer)
    print("Cricketer successfully added")


# Output single player details
def printPlayer(player):
        print(f"Name : {player["name"]}\nRuns : {player["runs"]}\nWickets : {player["wickets"]}\nOpponents : {player["Opponents"]}\n")

# View All Player Details
def viewOpponents():
    for player in Cricketers:
        printPlayer(player)
                  

# Search Induvidual Player
def searchPlayer():
    name = input("Enter Player Name: ")
    found = False
    for player in Cricketers:
     if name.lower() == player["name"].lower():
        printPlayer(player)
        found = True

    if not found:
        print("Player not found.")
        
    
# Updating runs of a player
def updateRuns():
    found = False
    name = input("Enter Player Name: ")
    updated_runs = int(input("Enter Updated Runs:"))
    for player in Cricketers:
        if name.lower() == player["name"].lower():
            player["runs"] = updated_runs
            found = True
            print("Runs successfully updated")
    if not found:
        print("Player not found.")        


# Retrieving Highest run scorer
def highestRunScorer():
    sorted_cricketer = sorted(Cricketers , key=lambda c:c["runs"])
    printPlayer(sorted_cricketer[-1])


# Menu for options
while(True):
    print("""========== Cricket Player Stats Manager ==========

1. Add Player
2. View All Players
3. Search Player
4. Update Runs
5. Show Highest Run Scorer
6. Exit""")
    choice = int(input("Enter Choice: "))
    
    match(choice):
        case 1 : addPlayer()
        case 2 : viewOpponents()
        case 3 : searchPlayer()
        case 4 : updateRuns()
        case 5 : highestRunScorer()
        case 6 : exit()