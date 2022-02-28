import subprocess

class TestQuestion2():
    def test_user_asks_to_put_5_people_into_1_group_prints_the_group(self):
        user_input = '\n'.join([
            '1',
            'Mary',
            'Lauren',
            'Awad',
            'Govind',
            'Isla',
            'stop',
            '1',
            'stop'
        ]).encode()

        expected_stdout = 'Mary, Lauren, Awad, Govind, Isla'

        stdout = run_question_2(user_input)
        
        assert stdout[-2] == expected_stdout

    def test_user_puts_0_people_into_1_group_and_stdouts_empty_group(self):
        user_input = '\n'.join([
            '1',
            'stop',
            '1',
            'stop'
        ]).encode()

        expected_stdout = ''

        stdout = run_question_2(user_input)
        
        assert stdout[-2] == expected_stdout
    
    def test_user_puts_5_people_into_3_groups_prints_all_3_groups(self):
        user_input = '\n'.join([
            '3',
            'Mary',
            'Lauren',
            'Awad',
            'Govind',
            'Isla',
            'stop',
            '1',
            '2',
            '3',
            'stop'
        ]).encode()

        expected_stdout = [
            'Enter a group number (NOT TESTED)',
            'Mary, Govind',
            'Enter a group number (NOT TESTED)',
            'Lauren, Isla',
            'Enter a group number (NOT TESTED)',
            'Awad',
            'Enter a group number (NOT TESTED)'
        ]

        stdout = run_question_2(user_input)

        assert stdout[-6] == expected_stdout[-6]
        assert stdout[-4] == expected_stdout[-4]
        assert stdout[-2] == expected_stdout[-2]

    def test_user_puts_0_people_into_3_groups_prints_all_3_groups(self):
        user_input = '\n'.join([
            '3',
            'stop',
            '1',
            '2',
            '3',
            'stop'
        ]).encode()

        expected_stdout = [
            'Enter a group number (NOT TESTED)',
            '',
            'Enter a group number (NOT TESTED)',
            '',
            'Enter a group number (NOT TESTED)',
            '',
            'Enter a group number (NOT TESTED)'
        ]
        stdout = run_question_2(user_input)

        assert stdout[-6] == expected_stdout[-6]
        assert stdout[-4] == expected_stdout[-4]
        assert stdout[-2] == expected_stdout[-2]


def run_question_2(user_input):
    """Run the Question 2 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(["python3",
            "chapter7/questions/question_2.py"], input=user_input)
            ).decode().strip().split('\n')