#Kóði gerður af Arnar Már Jónasson
#Start
valid_input = str()
x_loc = 1
y_loc = 1

def leaver()

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
        print("Victory!") 
        valid_input = "N"
        victory = True

    elif x_loc == 3 and y_loc == 2:
        print("You can travel: (N)orth or (S)outh.")
        valid_input = "N", "S"

    elif x_loc == 3 and y_loc == 3:
        print("You can travel: (S)outh or (W)est.")
        valid_input = "S", "W"

    return valid_input, victory

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



valid_input, victory = current_tile(position_x, position_y)
while victory == False:
    question = input("Direction: ")
    question = question.upper()
    if question not in valid_input:
        print("Not a valid direction!")
        valid_input, victory = current_tile(position_x, position_y)



    else:
        (position_x, position_y) = taple_value(question, position_x, position_y)
        valid_input, victory = current_tile(position_x, position_y)