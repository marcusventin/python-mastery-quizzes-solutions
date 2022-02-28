# Write a program that calculates the score for a word in Scrabble.
# It should:
# * Ask the user for a word e.g. `apple`.
# * Prints the score for the word in Scrabble by totalling the points
#   for each letter in the word.
#   * Points for each letter:
#     * 0 points: blank tile
#     * 1 point: E, A, I, O, N, R, T, L, S, U
#     * 2 points: D, G
#     * 3 points: B, C, M, P
#     * 4 points: F, H, V, W, Y
#     * 5 points: K
#     * 8 points: J, X
#     * 10 points: Q, Z

# * Note: You can assume that the user will enter a word that only
#   contains letters and blanks.  You can assume the word will be in
#   uppercase.

scores = {}
for key in ['E', 'A', 'I', 'O', 'N', 'R', 'T', 'L', 'S', 'U']:
    scores[key] = 1
for key in ['D', 'G']:
    scores[key] = 2
for key in ['B', 'C', 'M', 'P']:
    scores[key] = 3
for key in ['F', 'H', 'V', 'W', 'Y']:
    scores[key] = 4
scores['K'] = 5
for key in ['J', 'X']:
    scores[key] = 8
for key in ['Q', 'Z']:
    scores[key] = 10
scores[' '] = 0

score = 0

print("Enter a word to get its Scrabble score: ")
word = input()

for letter in word.upper():
    score += scores[letter]

print(score)