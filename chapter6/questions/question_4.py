# Write an adventure game that the player plays from the command line
# by typing in commands like `look`, `north` etc.  They can move
# between rooms, look at things and interact with objects.  The game
# should have this behaviour:
# * Two rooms: hall and study.
# * The player starts in the hall.
# * General commands (can be run at any time).
#   * `quit`: print `Bye!` and the program stops executing.
#   * (command incorrect for situation): nothing happens, nothing is
#                                        printed.
# * Room-specific commands
#   * Hall
#     * `look`: print `You are standing in a hall with a marble
#               floor. You see a door.`
#     * `north`: Move to the study.
#   * Study:
#     * `look`: print `You are in a warm and cosy study. You see a
#               safe. You see a desk.`
#     * `look at desk`: prints `You see a piece of paper that reads,
#                       The combination is 2451.`
#     * `south`: Move to the hall.
#     * `enter combination 2451`: print `You see some diamonds in
#                                 the safe, pick them up and make your
#                                 escape` and the program stops
#                                 executing.
#
# * Note: To stop the program (e.g. when the user types `quit` or when
#   they win the game), use the `break` keyword to exit a while loop early.
#   Other functions could break the automated tests.
#   
# * Note: When you run the automated tests, the tests will simulate
#   the user input. You shouldn't need to enter any input manually.
#   If the tests hang when you run them, it probably means your code
#   doesn't work correctly, yet.
# 
# * Note: To pass the tests, you'll need to print exactly what's
#   expected. Watch out for stray punctuation, capital letters, whitespace, etc.

room_number = 1
active = True
while active == True:
    if room_number == 1:
        while True:
            hall_move = input()
            if hall_move == "quit":
                print("Bye!")
                active = False
                break
            elif hall_move == "look":
                print("You are standing in a hall with a marble floor."
                        " You see a door.")
            elif hall_move == "north":
                room_number += 1
                break
    
    elif room_number == 2:
        while True:
            study_move = input()
            if study_move == "quit":
                print("Bye!")
                active = False
                break
            elif study_move == "look":
                print("You are in a warm and cosy study. You see a safe."
                    " You see a desk.")
            elif study_move == "look at desk":
                print("You see a piece of paper that reads,"
                    " The combination is 2451.")
            elif study_move == "south":
                room_number -= 1
                break
            elif study_move == "enter combination 2451":
                print("You see some diamonds in the safe, pick them up and"
                " make your escape")
                active = False
                break