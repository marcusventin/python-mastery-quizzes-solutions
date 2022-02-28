# Write a program that lets a user play a solo game of
# Blackjack. The program should:
# * Ask the player if they want to "hit" or "stick".
#   * If the player hits, add a card to their hand (which starts empty unlike 
#       real Blackjack)
#   * If the player sticks, end the game.
# * Keep asking the player if they want to "hit" or "stick" until they
#   say "stick".
# * Each time the player hits, calculate the score for the player's
#   hand and `puts` `Score so far: ` and the score.
#   * e.g. `Score so far: 23`
#   * A score is calculated by adding up the values of each of the
#     cards in the player's hand.
#   * Value for each card:
#     * "two": 2
#     * "three": 3
#     * "four": 4
#     * "five": 5
#     * "six": 6
#     * "seven": 7
#     * "eight": 8
#     * "nine": 9
#     * "ten": 10
#     * "jack": 10
#     * "queen": 10
#     * "king": 10
#     * "ace": 11 (This is slightly different from real Blackjack.)
# * When the game is over, print the outcome of the game.
#   * If the player's score is `<= 21`, print `You scored: ` and the
#     final score
#     * e.g. `You scored: 20`
#   * If the player's score is `> 21`, print `You busted with: ` and
#     the final score.
#     * e.g. `You busted with: 25`

# * As part of your solution, there should be four specific functions:
#   * `random_card`: This has already been written for you.  You don't
#     need to change it.
#   * `move`: Asks the player for a move.  If they enter `hit` or
#     `stick`, it returns the move.  If they enter something else, it
#     keeps asking them until they enter `hit` or `stick`.
#   * `score`: Takes an array of cards and returns the score for the
#     hand as an integer.
#   * `run_game`: uses the other methods to run a game of Blackjack.
#
# * Note: To stop the game when the user sticks, use the `break` keyword to
#   exit a while loop early. Don't use other keywords to quit the program 
#   because this might break the automated tests.
#
# * Note: When you run the automated tests, make sure to remove from
#   the top level of the file any calls to `run_test` or any other
#   methods.

# You don't need to change this method!
import random
def random_card():
    cards = ["two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten",
            "jack", "queen", "king", "ace"]
    return cards[random.randint(0, 12)]

def move():
    print('Hit or stick? ')
    user_move = input()
    while user_move != 'hit' and user_move != 'stick':
        user_move = input()
    if user_move == 'hit':
        print('hit')
        return(user_move)
    elif user_move == 'stick':
        print('stick')
        return(user_move)

def score(hand):
    values = {
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'jack': 10,
        'queen': 10,
        'king': 10,
        'ace': 11
    }

    return(sum([values[card] for card in hand]))

def run_game():
    hand = []
    user_choice = move()
    while user_choice != 'stick':
        hand.append(random_card())
        print(f"Score so far: {score(hand)}")
        user_choice = move()
    if score(hand) <= 21:
        print(f"You scored: {score(hand)}")
    elif score(hand) > 21:
        print(f"You busted with: {score(hand)}")
