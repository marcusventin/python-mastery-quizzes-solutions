import subprocess

class TestQuestion3():
    def test_user_inputs_sport_as_characteristic_to_group_people_by(self):
        user_input = 'sport'.encode()
        expected_stdout = [
            "squash",
            "Mary",
            "Lauren",
            "Govind",
            "weightlifting",
            "Isla",
            "Awad",
            "cycling",
            "Sam",
            "Will"
        ]

        stdout = run_question_3(user_input)

        assert stdout[-10:] == expected_stdout
    
    def test_user_inputs_fruit_as_characteristic_to_group_people_by(self):
        user_input = 'fruit'.encode()

        expected_stdout = [
            "blackberry",
            "Mary",
            "Will",
            "orange",
            "Lauren",
            "Sam",
            "banana",
            "Isla",
            "Govind",
            "kiwi",
            "Awad"
        ]

        stdout = run_question_3(user_input)

        assert stdout[-11:] == expected_stdout


def run_question_3(user_input):
    """Run the Question 3 program with user_input, returning the stdout as a
    list of strings stripped of whitespace, with each list entry corresponding 
    to a line of stdout.
    """
    return(subprocess.check_output(['python3',
            'chapter8/questions/question_3.py'], input=user_input
            ).decode().strip().split('\n'))