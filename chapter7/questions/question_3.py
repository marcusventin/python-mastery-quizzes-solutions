# Write a game where the player swims down a river infested with
# crocodiles.  The game should:
# * Use the `river` variable that defines the river (see code below).
#   * `-`: clear water.
#   * `C`: crocodile.
#   * The first five characters represent the first part of the river.
#     The second five characters represent the second part of the
#     river.  And so on.
# * Define the player as one character wide.
# * Start the player at the central position of the first part of the
#   river.
#   * e.g. `C-P--`.
# * Each turn:
#   * Check to see if the player is in the same position as a
#     crocodile.  If they are, print `You were eaten.' and stop the
#     program.
#   * print the whole river.  Include a `P` where the player is.
#   * Ask the player if they want to go to left, right or neither.
#     The player enters `left`, `right` or `neither`.
#   * Make the player float down the river by one river part (one line
#     of digits).  Move them to the left, the right, or keep them
#     where they are.
# Print `You survived!` if the player makes it past all parts of the
# river without hitting a crocodile.
#
# * Note: To stop the game when the user is eaten or survives the
#   whole river, use the `break` keyword to exit a while loop early.
#   Other functions might break the automated tests.   
#
# * Note: You can assume the player will never move outside the
#   boundary of the river when they choose left and right.  You can
#   also assume the player will always enter either `left`, `right` or
#   `neither`.
#
# * Example output:
#   ```
#   --P--
#   --C--
#   CC-CC
#   CC-CC
#   Type left, right or neither
#   left
#   -----
#   -PC--
#   CC-CC
#   CC-CC
#   Type left, right or neither
#   right
#   -----
#   --C--
#   CCPCC
#   CC-CC
#   Type left, right or neither
#   neither
#   -----
#   --C--
#   CC-CC
#   CCPCC
#   Type left, right or neither
#   neither
#   You survived!
#   ```

turn = 0
player_position = 2

river_original = ['-----', '--C--', 'CC-CC', 'CC-CC']

while True:
    if turn >= 4:
        print("You survived!")
        break
    else:
        # Makes a copy of the original river to prevent overwriting.
        river = river_original[:]
        if river[turn][player_position] == 'C':
            print("You were eaten.")
            break

        river[turn] = (river[turn][:player_position] + "P" + 
            river[turn][player_position + 1:])
        for line in river:
            print(line)

        while True:
            print('Type left, right or neither ')
            player_move = input()
            if player_move == 'right':
                player_position += 1
                turn += 1
                break
            elif player_move == 'left':
                player_position -= 1
                turn += 1
                break
            elif player_move == 'neither':
                turn += 1
                break
    