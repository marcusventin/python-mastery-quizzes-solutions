import subprocess

class TestQuestion2():
    def test_user_inputs_sport_as_category_and_squash_as_value(self):
        user_input = '\n'.join(
            ['sport', 'squash']
            ).encode()

        expected_stdout = [
            'Mary',
            'Lauren',
            'Govind'
        ]

        stdout = run_question_2(user_input)

        assert stdout[-3:] == expected_stdout
    
    def test_user_inputs_fruit_as_category_and_kiwi_as_value(self):
        user_input = '\n'.join(
            ['fruit', 'kiwi']
            ).encode()

        expected_stdout = 'Awad'

        stdout = run_question_2(user_input)

        assert stdout[-1] == expected_stdout
        
    
    def test_user_inputs_fruit_as_category_and_mango_as_value(self):
        user_input = '\n'.join(
            ['fruit', 'mango']
            ).encode()

        expected_stdout = ''

        # In this case, we expect the program to return nothing - nobody chose 
        # mango as their favourite fruit. The .strip() function called in 
        # .run_question_2() removes whitespace, so we need to use a bespoke
        # function that does not strip out whitespace.
        stdout = subprocess.check_output(['python3',
            'chapter8/questions/question_2.py'], input=user_input
            ).decode().split('\n')
        
        assert stdout[-1] == expected_stdout


def run_question_2(user_input):
    """Run the Question 2 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(['python3',
            'chapter8/questions/question_2.py'], input=user_input
            ).decode().strip().split('\n'))