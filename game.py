from msilib.schema import Directory


def main():

    print("Welcome to my game!")
    Player_name = input("What is your name?")
    print(" Hi " + Player_name)
    lives = 3
    
    print(f" you have {lives} lives remaining ")

    backpack = [] #intitalise empty list for backpack
    print("there are 4 directions to choose from North, East, South, West")

    while True:

        player_direction = input("Which direction do you want to go?")

        if player_direction == "North":
            room_direction = "North"
            puzzle = "What is 7+7? "
            puzzle_solution = "14"
            key_number = "1"
            lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
            
        
        elif player_direction == "South":
            room_direction = "South "
            puzzle = "What is 5+5?"
            puzzle_solution = "10"
            key_number = "2"
            lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
            
            
        
        elif player_direction == "East":
            room_direction = "East"
            puzzle = "What is 9+9? "
            puzzle_solution = "18"
            Key_number = "3"
            lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
            
                

                 
        elif player_direction == "West":
            room_direction = "West"
            puzzle = "What is 6+6? "
            puzzle_solution = "12"
            Key_number = "4"
            lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
            
                  
        
        else:
            print("invalid response")

        
        # if backpack is full, open door, win game
        if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("Key 4" in backpack):
            print("Door open, Win game")
            exit()
        
        if lives ==0:
            print("Sorry, you died")
            exit()

def in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number):
    print(f"You entered the {room_direction} Room.")
    puzzle_guess = input(puzzle)
    if puzzle_guess == puzzle_solution:
        print(f"Correct. Key {key_number} collected.")
        backpack.append(f"Key {Key_number}")
    else:
        lives -= 1
        print(f"you have lost a life, you now have {lives} remaining ")
        
    return lives 

main()