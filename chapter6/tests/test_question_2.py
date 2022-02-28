import subprocess

class TestQuestion2():
    def test_player_1_rock_player_2_rock(self):
        user_input = '\n'.join(
            ['rock', 'rock']
            ).encode()
        expected_stdout = "It's a draw"

        stdout = run_question_2(user_input)
            
        assert stdout[-1] == expected_stdout

    def test_player_1_paper_player_2_paper(self):
        user_input = '\n'.join(
            ['paper', 'paper']
            ).encode()
        expected_stdout = "It's a draw"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout
    
    def test_player_1_scissors_player_2_scissors(self):
        user_input = '\n'.join(
            ['scissors', 'scissors']
            ).encode()
        expected_stdout = "It's a draw"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout
    
    def test_player_1_rock_player_2_scissors(self):
        user_input = '\n'.join(
            ['rock', 'scissors']
            ).encode()
        expected_stdout = "Player 1 wins"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout
    
    def test_player_1_paper_player_2_rock(self):
        user_input = '\n'.join(
            ['paper', 'rock']
            ).encode()
        expected_stdout = "Player 1 wins"

        stdout = run_question_2(user_input)
        
        assert expected_stdout == stdout[-1]
    
    def test_player_1_scissors_player_2_paper(self):
        user_input = '\n'.join(
            ['scissors', 'paper']
            ).encode()
        expected_stdout = "Player 1 wins"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout
    
    def test_player_1_rock_player_2_paper(self):
        user_input = '\n'.join(
            ['rock', 'paper']
            ).encode()
        expected_stdout = "Player 2 wins"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout
    
    def test_player_1_paper_player_2_scissors(self):
        user_input = '\n'.join(
            ['paper', 'scissors']
            ).encode()
        expected_stdout = "Player 2 wins"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout
    
    def test_player_1_scissors_player_2_rock(self):
        user_input = '\n'.join(
            ['scissors', 'rock']
            ).encode()
        expected_stdout = "Player 2 wins"

        stdout = run_question_2(user_input)
        
        assert stdout[-1] == expected_stdout


def run_question_2(user_input):
    """Run the Question 2 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(["python3",
            "chapter6/questions/question_2.py"],
            input=user_input).decode().strip().split("\n"))