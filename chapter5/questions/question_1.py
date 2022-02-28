# Write a program that acts like a magic 8 ball.  It should:
# * Randomly choose one of five predictions:
#   * `It is certain`
#   * `It is decidedly so`
#   * `Ask again later`
#   * `Outlook not so good`
#   * `Very doubtful`
# * print the prediction it chose.
# * Example output from running the program several times:
#   $ python3 chapter5/questions/question_1.py
#   Ask again later
#   $ python3 chapter5/questions/question_1.py
#   Ask again later
#   $ python3 chapter5/questions/question_1.py
#   It is certain

import random

responses = ["It is certain",
            "It is decidedly so",
            "Ask again later",
            "Outlook not so good",
            "Very doubtful"]

print(random.choice(responses))