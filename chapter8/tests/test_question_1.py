import subprocess
import string

class TestQuestion1():
    def test_word_with_3_blanks(self):
        user_input = '  A '.encode()
        expected_stdout = '1'

        stdout = run_question_1(user_input)

        assert stdout[-1] == expected_stdout

    def test_word_with_all_letters_in_the_alphabet(self):
        # string.ascii_uppercase returns all the letters of the alphabet in 
        # uppercase.
        user_input = string.ascii_uppercase.encode()

        expected_stdout = '87'

        stdout = run_question_1(user_input)

        assert stdout[-1] == expected_stdout
    
    def test_word_with_repeated_letters(self):
        user_input = 'GOOD'.encode()
        expected_stdout = '6'

        stdout = run_question_1(user_input)

        assert stdout[-1] == expected_stdout


def run_question_1(user_input):
    """Run the Question 1 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(['python3',
            'chapter8/questions/question_1.py'], input=user_input
            ).decode().strip().split('\n'))