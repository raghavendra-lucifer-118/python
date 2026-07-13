import random

#Intialise values
value = random.randint(0,11)
attempts = 1

# Simple menu
print("1.Start Game")
print("2.Exit Game")

# Take choice in while loop for guess
game_choice = int(input("Choose option: "))
match(game_choice):
    # Enter game if choosen 1
    case 1:
        while(True):
            user_guess = int(input("Your Guess: "))
            if(user_guess == value):
                print(f"Right guess in {attempts} attempts")
                exit()
            elif(user_guess > value):
                print("Too High.... Try again")
                attempts += 1
            else:
                print("Too low... Try again")        
                attempts += 1
         
    # Exit game if choosen 2     
    case 2:
        print("Exiting game...")
        exit()

