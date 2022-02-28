# Write a program that lets two players play Rock, Paper, Scissors. The program 
# should:
# * Ask player 1 for their move.  They can input `rock`, `paper` or
#   `scissors`.
# * Ask player 2 for their move.  They can input `rock`, `paper` or
#   `scissors`.
# * Calculate who has won.  `rock` beats `scissors`, `paper` beats
#   `rock`, `scissors` beat `paper`.
# * If player 1 has won, print `Player 1 wins`.
# * If player 2 has won, print `Player 2 wins`.
# * If the game is a draw, print `It's a draw`.
#
# * Note: You can assume that players will input one of the three
#   possible moves described above.
#
# * Note: When you run the automated tests, the tests will simulate
#   the user input.  You shouldn't need to enter any input manually.
#   If the tests hang when you run them, it probably means your code
#   doesn't work correctly, yet.
#
# * Note: You can assume the players will only ever input `rock`,
#   `paper` or `scissors`.

print("Player 1, make your move: \n")
p1_move = input()

print("\nPlayer 2, make your move: \n")
p2_move = input()

if p1_move == p2_move:
    print("It's a draw")
elif (p1_move == "rock" and p2_move == "scissors") or (p1_move == "paper" and 
    p2_move == "rock") or (p1_move == "scissors" and p2_move == "paper"):
    print("Player 1 wins")
elif (p1_move == "rock" and p2_move == "paper") or (p1_move == "paper" and 
    p2_move == "scissors") or (p1_move == "scissors" and p2_move == "rock"):
    print("Player 2 wins")