import subprocess

class TestQuestion3():
    def test_player_inputs_neither(self):
        user_input = 'neither'.encode()

        expected_stdout = [
            "--P--",
            "--C--",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "You were eaten."
        ]

        stdout = run_question_3(user_input)

        # We aren't testing for the wording of the input request message, so we
        # slice around this to test for river formatting and game over messages.
        assert stdout[0:4] == expected_stdout[0:4]
        assert stdout[-1] == expected_stdout[-1]
    
    def test_player_inputs_right_neither(self):
        user_input = '\n'.join(
            ['right', 'neither']
            ).encode()

        expected_stdout = [
            "--P--",
            "--C--",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "-----",
            "--CP-",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "You were eaten."   
        ]

        stdout = run_question_3(user_input)
        
        assert stdout[0:4] == expected_stdout[0:4]
        assert stdout[5:9] == expected_stdout[5:9]
        assert stdout[-1] == expected_stdout[-1]
  
    def test_player_inputs_right_left_neither(self):
        user_input = '\n'.join(
            ['right', 'left', 'right']
            ).encode()

        expected_stdout = [
            "--P--",
            "--C--",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "-----",
            "--CP-",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "-----",
            "--C--",
            "CCPCC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "You were eaten."
        ]

        stdout = run_question_3(user_input)

        assert stdout[0:4] == expected_stdout[0:4]
        assert stdout[5:9] == expected_stdout[5:9]
        assert stdout[10:14] == expected_stdout[10:14]
        assert stdout[-1] == expected_stdout[-1]

    def test_player_moves_left_right_neither_neither(self):
        user_input = '\n'.join(
            ['left', 'right', 'neither', 'neither']
            ).encode()

        expected_stdout = [
            "--P--",
            "--C--",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "-----",
            "-PC--",
            "CC-CC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "-----",
            "--C--",
            "CCPCC",
            "CC-CC",
            "Type left, right or neither (NOT TESTED)",
            "-----",
            "--C--",
            "CC-CC",
            "CCPCC",
            "You survived!"
        ]

        stdout = run_question_3(user_input)

        assert stdout[0:4] == expected_stdout[0:4]
        assert stdout[5:9] == expected_stdout[5:9]
        assert stdout[10:14] == expected_stdout[10:14]
        assert stdout[15:19] == expected_stdout[15:19]
        assert stdout[-1] == expected_stdout[-1]


def run_question_3(user_input):
    """Run the Question 3 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(["python3",
            "chapter7/questions/question_3.py"], input=user_input
            ).decode().strip().split('\n'))