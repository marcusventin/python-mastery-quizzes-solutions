import subprocess

class TestQuestion1():
    def test_user_enters_10(self):
        user_input = '10'.encode()
        expected_stdout = '----------'

        stdout = run_question_1(user_input)

        assert stdout[-1] == expected_stdout
    
    def test_user_enters_10_4_2_7_5_1(self):
        user_input = '10,4,2,7,5,1'.encode()
        expected_stdout = [
            '----------',
            '----',
            '--',
            '-------',
            '-----',
            '-'
        ]

        stdout = run_question_1(user_input)
        print(stdout)
        
        # Slice the last 6 lines of stdout.
        assert stdout[-6:] == expected_stdout


def run_question_1(user_input):
    """Run the Question 1 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(['python3',
            'chapter7/questions/question_1.py'], input=user_input
            ).decode().strip().split('\n'))