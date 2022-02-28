# Python Mastery Quizzes Solutions

## Motivation
This repo is a companion to the Python Mastery Quizzes. It is intended to provide inspiration to anyone stuck on the mastery quizzes. It must be noted that the solutions presented here represent only one way of passing the quizzes, and should not be viewed as ideal or optimal solutions.

## How to Use
View the solutions online. 
  
OR  
1. Alternatively, fork this repo and clone it to your local machine.
2. Set up a virtual environment with:
    `python3 -m venv venv`
    `. venv/bin/activate`
3. Mess around with the solutions.
4. To check the solutions against the automated tests, enter into your terminal:  
`python -m pytest CHAPTERFOLDER/tests`  
e.g., to run tests on Chapter 1, you would enter:  
`python -m pytest chapter1/tests`  

If you want to run tests on a specific question, you can enter:  
`python -m pytest CHAPTERFOLDER/tests/TEST_QUESTION_NUMBER.py`  
e.g., to run tests on Question 2 of Chapter 4, you would enter:  
`python -m pytest chapter4/tests/test_question_2.py`  
