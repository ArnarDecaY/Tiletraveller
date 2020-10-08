#Kóði gerður af Arnar Már Jónasson
#Start
import random
valid_input = str()
x_loc = 1
y_loc = 1
coin_count = 0
list_tuple = [(1,2),(2,2),(2,3),(3,2)]
Moves_counter = 0

YES = "y"
NO = "n"

NORTH = "n"
EAST = "e"
SOUTH = "s"
WEST = "w"


def lever(coin_count):
    while True:
        lever = random.choice([YES, NO])
        print(f"Pull a lever (y/n): {lever}")
        lever = lever.lower()
        if not lever in 'yn':
            print("Invalid input")
            continue
        if lever == 'y':
            coin_count += 1
            print(f"You received 1 coin, your total is now {coin_count}.")
            break
        elif lever == 'n':
            break
    return coin_count

def lever_checking(x_loc, y_loc, coin_count):
    for i in list_tuple:
        if (x_loc,y_loc) == i:
            coin_count = lever(coin_count)
    return coin_count

def play_again():
    while True:
        play_again = str(input("Play again (y/n): "))
        if not play_again in 'yn':
            print("Invalid input")
            continue
        if play_again == 'y':
            return True
        elif play_again == 'n':
            exit()

def current_tile(x_loc, y_loc):
    victory = False
    if x_loc == 1 and y_loc == 1:
        print("You can travel: (N)orth.")
        valid_input = "n", "N"

    elif x_loc == 1 and y_loc == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        valid_input = "N", "E", "S"  

    elif x_loc == 1 and y_loc == 3:
        print("You can travel: (E)ast or (S)outh.")
        valid_input = "E", "S"

    elif x_loc == 2 and y_loc == 1:
        print("You can travel: (N)orth.") 
        valid_input = "N"

    elif x_loc == 2 and y_loc == 2:
        print("You can travel: (S)outh or (W)est.")
        valid_input = "S", "W"

    elif x_loc == 2 and y_loc == 3:
        print("You can travel: (E)ast or (W)est.")
        valid_input = "E", "W"

    elif x_loc == 3 and y_loc == 1:
        print(f"Victory! Total coins {coin_count}. Moves {Moves_counter}") 
        valid_input = "N"
        victory = True

    elif x_loc == 3 and y_loc == 2:
        print("You can travel: (N)orth or (S)outh.")
        valid_input = "N", "S"

    elif x_loc == 3 and y_loc == 3:
        print("You can travel: (S)outh or (W)est.")
        valid_input = "S", "W"

    return valid_input, victory, 

def taple_value(character, pos_x, pos_y):
    if character == "E":
        pos_x += 1
    elif character == "S":
        pos_y -= 1
    elif character == "W":
        pos_x -= 1
    elif character == "N":
  	    pos_y += 1
    return pos_x, pos_y
    
position_x, position_y = 1, 1

victory = False

seed = int(input("Input seed: "))
random.seed(seed)

valid_input, victory = current_tile(position_x, position_y)
while victory == False:
    question = random.choice([NORTH, EAST, SOUTH, WEST])
    print(f"Direction: {question}")
    question = question.upper()
    if question not in valid_input:
        print("Not a valid direction!")
        valid_input, victory = current_tile(position_x, position_y)

    else:
        Moves_counter += 1
        (position_x, position_y) = taple_value(question, position_x, position_y)
        coin_count = lever_checking(position_x, position_y, coin_count)
        valid_input, victory = current_tile(position_x, position_y)
    
    if victory == True:
        reapet = play_again()
        if reapet == True:
            Moves_counter = 0
            coin_count = 0
            victory = False
            position_x, position_y = 1, 1
            valid_input, victory = current_tile(position_x, position_y)
