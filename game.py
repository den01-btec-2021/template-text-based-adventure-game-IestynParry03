from tkinter import W


def main():
    print("Welcome to my game!")
    Player_name = input("What is your name?")
    print(" Hi " + Player_name)
    Lives = 3
    
    print(f" you have {Lives} lives remaining ")

    backpack = [] #intitalise empty list for backpack
    print("there are 4 directions to choose from North, East, South, West")

    while True:

        player_direction = input("Which direction do you want to go?")

        if player_direction == "North":
            print ("you went North")
            puzzle_guess_north = input("What is 2+2?")
            if puzzle_guess_north == "4":
                print("correct")
            
                backpack.append("Key 1")
                # need to collect something here
            else:
                print("Incorrect")
                Lives -= 1
                print(f"you have lost a life, you now have {Lives} remaining remaining ")
        elif player_direction == "South":
            print("you went South")
        elif player_direction == "East":
            print("you went East")
        elif player_direction == "West":
            print("you went West")
        else:
            print("invalid response")

        # if backpack is full, open door, win game
        if ("Key 1" in backpack) and ("Key 2") in backpack) and ("Key 3 in backpack") and ("Key 4") in backpack):
            print("Door open! Win game!")
            
        if Lives ==0:
            print("Sorry, you died")
            exit()



main()