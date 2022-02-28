import subprocess

class TestQuestion1():
    def test_user_enters_just_stop(self):
        # We save the user's input in the bytes format.
        user_input = 'stop'.encode()
        expected_stdout = '0'

        stdout = run_question_1(user_input)
        
        assert stdout[-1] == expected_stdout
        
    def test_user_enters_3_and_stop(self):
        # A more readable way of writing '3\nstop'.
        user_input = '\n'.join(
            ['3', 'stop']
            ).encode()
        expected_stdout = '3'

        stdout = run_question_1(user_input)
        
        assert stdout[-1] == expected_stdout

    def test_user_enters_5_4_5_2_1_and_stop(self):
        user_input = '\n'.join(
            ['5', '4', '3', '2', '1', 'stop']
            ).encode()
        expected_stdout = '15'

        stdout = run_question_1(user_input)
        
        assert stdout[-1] == expected_stdout


def run_question_1(user_input):
    """Run the Question 1 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    # We add user input to our subprocess call and save the output. We 
    # convert the output from bytes to string. We strip out whitespace and split
    # the output into a list, where each item corresponds to a line in the 
    # stdout.
    return(subprocess.check_output(["python3",
            "chapter6/questions/question_1.py"],
            input=user_input).decode().strip().split("\n"))