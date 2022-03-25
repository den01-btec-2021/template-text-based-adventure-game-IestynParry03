from audioop import add
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
            key_number = "3"
            lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
            
                

                 
        elif player_direction == "West":
            room_direction = "West"
            puzzle = "What is 6+6? "
            puzzle_solution = "12"
            key_number = "4"
            lives = in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number)
            
                  
        
        else:
            print("invalid response")

        
        # if backpack is full, open door, win game
        if ("Key 1" in backpack) and ("Key 2" in backpack) and ("Key 3" in backpack) and ("Key 4" in backpack):
            print("Congrations you have collected all keys and won the game!")
            exit()
        
        if lives ==0:
            print("Sorry, you died")
            exit()

def in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number):
    print(f"You entered the {room_direction} Room.")
    puzzle_guess = input(puzzle)
    if puzzle_guess == puzzle_solution:
        print(f"Correct. Key {key_number} collected.")
        if f"Key {key_number}" not in backpack:
            backpack.append(f"Key {key_number}")
        else:
            print("You have already collected this Key!")
    else:
        lives -= 1
        print(f"you have lost a life, you now have {lives} remaining ")
        
    return lives

def addition(a,b):
    return a+b

def test_addition():
    assert addition(3,5) == 8
    assert addition(-1,0) == -1
    assert addition(-1,1) == 0

def test_in_room():

    backpack = []
    lives = 3
    room_direction = "North"
    puzzle = "What is 6 + 6?"
    puzzle_solution = "12"
    key_number = "1"

    #check correct??
    assert in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number) == 2 # lives -1
    assert f"Key {key_number}" in backpack #check that this key is the backpack is in the backpack
    
    
    in_room(backpack,lives,room_direction,puzzle,puzzle_solution,key_number) == 3
    assert backpack != ["Key 1","Key 1"]
    
    
    if __name__ == "__main__":
        
        #main()
        #value = addition(3,2)
        #print(value)
        test_addition()