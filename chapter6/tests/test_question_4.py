import subprocess

class TestQuestion4():
    def test_immediately_quit(self):
        user_input = 'quit'.encode()
        expected_stdout = ["Bye!"]

        stdout = run_question_4(user_input)

        assert stdout == expected_stdout
    
    def test_look_quit(self):
        user_input = '\n'.join(
            ['look', 'quit']
            ).encode()

        expected_stdout = [
            "You are standing in a hall with a marble floor. You see a door.",
            "Bye!"
            ]
            
        stdout = run_question_4(user_input)
        
        assert stdout == expected_stdout
    
    def test_look_incorrect_command_in_hall_quit(self):
        user_input = '\n'.join(
            ['look', 'blah', 'quit']
            ).encode()

        expected_stdout = [
            "You are standing in a hall with a marble floor. You see a door.",
            "Bye!"
            ]

        stdout = run_question_4(user_input)
        
        assert stdout == expected_stdout
    
    def test_north_to_study_look_quit(self):
        user_input = '\n'.join(
            ['north', 'look', 'quit']
            ).encode()

        expected_stdout = [
            "You are in a warm and cosy study. You see a safe. You see a desk.",
            "Bye!"
            ]

        stdout = run_question_4(user_input)
        
        assert stdout == expected_stdout
    
    def test_north_to_study_look_incorrect_command_quit(self):
        user_input = '\n'.join(
            ['north', 'look', 'blah', 'quit']
            ).encode()

        expected_stdout = [
            "You are in a warm and cosy study. You see a safe. You see a desk.",
            "Bye!"
            ]

        stdout = run_question_4(user_input)

        assert stdout == expected_stdout
    
    def test_go_between_hall_and_study_many_times_look_each_time_quit(self):
        user_input = '\n'.join([
            'look',
            'north',
            'look',
            'south',
            'look', 
            'north',
            'look',
            'south',
            'look', 
            'quit'
            ]).encode()

        expected_stdout = [
            "You are standing in a hall with a marble floor. You see a door.",
            "You are in a warm and cosy study. You see a safe. You see a desk.",
            "You are standing in a hall with a marble floor. You see a door.",
            "You are in a warm and cosy study. You see a safe. You see a desk.",
            "You are standing in a hall with a marble floor. You see a door.",
            "Bye!"
        ]

        stdout = run_question_4(user_input)
        
        assert stdout == expected_stdout
    
    def test_north_to_study_look_at_desk_quit(self):
        user_input = '\n'.join(
            ['north', 'look at desk', 'quit']
            ).encode()

        expected_stdout = [
            "You see a piece of paper that reads, The combination is 2451.",
            "Bye!"
            ]

        stdout = run_question_4(user_input)
        
        assert stdout == expected_stdout
    
    def test_north_to_study_enter_combination(self):
        user_input = '\n'.join(
            ['north', 'enter combination 2451']
            ).encode()

        expected_stdout = [
            ("You see some diamonds in the safe, pick them up and make"
            " your escape")
            ]

        stdout = run_question_4(user_input)

        assert stdout == expected_stdout


def run_question_4(user_input):
    """Run the Question 4 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(["python3",
            "chapter6/questions/question_4.py"], input=user_input
            ).decode().strip().split("\n"))