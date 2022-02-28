import subprocess

class TestQuestion3():
    def test_move_north_to_cave_move_north_to_win(self):
        user_input = '\n'.join(
            ['north', 'north']
            ).encode()
            
        expected_stdout = [
            "You are in a scary cave.",
            "You walk into sunlight."
            ]
                            
        stdout = run_question_3(user_input)
        
        assert stdout == expected_stdout
    
    def test_incorrect_command_in_passage_move_north_to_cave_move_north(self):
        user_input = '\n'.join(
            ['blah', 'north', 'north']
            ).encode()

        expected_stdout = [
            "You are in a scary cave.",
            "You walk into sunlight."
            ]

        stdout = run_question_3(user_input)

        assert stdout == expected_stdout
    
    def test_move_north_and_south_several_times_then_north_twice(self):
        user_input = '\n'.join([
            'north',
            'south',
            'north',
            'south',
            'north', 
            'south',
            'north',
            'north'
            ]).encode()

        expected_stdout = [
            "You are in a scary cave.",
            "You are in a scary passage.",
            "You are in a scary cave.",
            "You are in a scary passage.",
            "You are in a scary cave.",
            "You are in a scary passage.",
            "You are in a scary cave.",
            "You walk into sunlight."
            ]

        stdout = run_question_3(user_input)

        assert stdout == expected_stdout
    
    def test_move_north_to_cave_incorrect_command_in_cave_move_north(self):
        user_input = '\n'.join(
            ['north', 'blah', 'north']
            ).encode()

        expected_stdout = [
            "You are in a scary cave.",
            "You walk into sunlight."
            ]

        stdout = run_question_3(user_input)

        assert stdout == expected_stdout



def run_question_3(user_input):
    """Run the Question 3 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(["python3", 
            "chapter6/questions/question_3.py"], input=user_input
            ).decode().strip().split("\n"))