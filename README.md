# Python Mastery Quizzes Solutions

## Motivation
This repo is a companion to the [Python Mastery Quizzes](https://github.com/marcusventin/python-mastery-quizzes). It is intended to provide inspiration to anyone stuck on the mastery quizzes. It must be noted that the answers presented here represent only one way of passing the quizzes, and should not be viewed as ideal or optimal solutions.

## How to Use
#### Set-Up
View the solutions online. 
  
OR  
  
1. Fork this repo and clone it to your local machine.
2. Make sure that you have Python installed.
    * If you don't, download it from [Python.org](https://www.python.org/)
4. In your terminal, navigate to the project's root directory and set up a virtual environment with:
<br>`. venv/bin/activate`
6. Mess around with the solutions.

#### Testing
* To check the solutions against the automated tests, navigate to the project's root directory and enter into your terminal:  
`python -m pytest CHAPTERFOLDER/tests`  
e.g., to run tests on Chapter 1, you would enter:  
`python -m pytest chapter1/tests`  

* If you want to run tests on a specific question, you can enter:  
`python -m pytest CHAPTERFOLDER/tests/TEST_QUESTION_NUMBER.py`  
e.g., to run tests on Question 2 of Chapter 4, you would enter:  
`python -m pytest chapter4/tests/test_question_2.py`  
