def main():
    print("Welcome to my game!")
    Player_name = input("What is your name?")
    print(" Hi " + Player_name)
    Lives = 3
    print(f" you have {Lives} remaining ")
    print("there are 4 directions to choose from North, East, South, West")
    player_direction = input("which direction do you want to go?")
    if player_direction == "North":
        print ("you went North")
    elif player_direction == "South":
        print("you went South")
    elif player_direction == "East":
        print("you went East")
    elif player_direction == "West":
        print("you went West")
    else:
        print("invalid response")



main()