# Write an adventure game that the player plays from the command line
# by typing in the commands `north` and `south`.  The game should have
# this behaviour:
# * Two rooms: a passage and a cave.
#   * Passage commands
#     * `north`: prints `You are in a scary cave.`
#   * Cave commands
#     * `south`: prints `You are in a scary passage.`
#     * `north`: prints 'You walk into sunlight.` and the program
#                stops executing.
# * The player starts in the passage.
# * When the player starts the game, the game shouldn't print a room
#   description until the player moves between rooms.
# * If the player enters a command that is incorrect for the
#   situation, nothing happens and nothing is printed.
#
# * Note: To stop the program when the user wins, use the `break` keyword. 
#   Other functions might break the automated tests.
#
# * Note: When you run the automated tests, the tests will simulate
#   the user input.  You shouldn't need to enter any input manually.
#   If the tests hang when you run them, it probably means your code
#   doesn't work correctly, yet.
# 
# * Note: To pass the tests, you'll need to print exactly what's
#   expected. Watch out for stray punctuation, whitespace, capital letters, etc.

room_counter = 1

while True:
    start_choice = input()
    if start_choice == "north":
        room_counter += 1
        break

while True:
    if room_counter == 1:
        print("You are in a scary passage.")
        while True:
            passage_choice = input()
            if passage_choice == "north":
                room_counter += 1
                break
    elif room_counter == 2:
        print("You are in a scary cave.")
        while True:
            cave_choice = input()
            if cave_choice == "north":
                room_counter += 1
                break
            elif cave_choice == "south":
                room_counter -= 1
                break
    elif room_counter == 3:
        print("You walk into sunlight.")
        break

