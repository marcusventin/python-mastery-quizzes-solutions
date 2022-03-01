import random
from unittest.mock import patch

import chapter9.questions.question_1 as program
path = 'chapter9.questions.question_1'


class TestQuestion1():
    # To patch the random.randint function, we create the patch as a decorator
    # outside our test and then define its return values within the test. If we 
    # were only making one assertion in this test, we could define the return 
    # value by adding 'return_value=x' when creating the patch.
    # We use patch.object() rather than patch() because we only want to mock
    # one method of the random module, rather than the entire module.
    @patch.object(random, 'randint')
    def test_random_card_returns_all_cards_in_the_suit(self, mock_randint):
        mock_randint.return_value = 0
        assert program.random_card() == 'two'

        mock_randint.return_value = 1
        assert program.random_card() == 'three'

        mock_randint.return_value = 2
        assert program.random_card() == 'four'

        mock_randint.return_value = 3
        assert program.random_card() == 'five'

        mock_randint.return_value = 4
        assert program.random_card() == 'six'

        mock_randint.return_value = 5
        assert program.random_card() == 'seven'

        mock_randint.return_value = 6
        assert program.random_card() == 'eight'

        mock_randint.return_value = 7
        assert program.random_card() == 'nine'

        mock_randint.return_value = 8
        assert program.random_card() == 'ten'

        mock_randint.return_value = 9
        assert program.random_card() == 'jack'

        mock_randint.return_value = 10
        assert program.random_card() == 'queen'

        mock_randint.return_value = 11
        assert program.random_card() == 'king'

        mock_randint.return_value = 12
        assert program.random_card() == 'ace'

    # Using patch here allows us to mock any instance of the input() function 
    # and set a return value within the decorator. patch.object doesn't work 
    # because we've defined the path as a program, and pytest cannot find a
    # module called program.
    @patch(f'{path}.input', return_value='hit')
    def test_move_hit_returns_hit(self, mock_input, capsys):
        expected_stdout = 'hit'

        program.move()
        stdout = capture_stdout(capsys)

        assert stdout[-1] == expected_stdout
    
    @patch(f'{path}.input', return_value='stick')
    def test_move_stick_returns_stick(self, mock_input, capsys):
        expected_stdout = 'stick'

        program.move()
        stdout = capture_stdout(capsys)

        assert stdout[-1] == expected_stdout

    @patch(f'{path}.input')
    def test_move_user_inputs_blah_then_a_valid_move(self, mock_input, capsys):
        # The side_effect attribute allows us to set a different return value 
        # each time the mocked function is called. It can be included within the
        # decorator.
        mock_input.side_effect = ['blah', 'hit']
        expected_stdout = 'hit'
        
        program.move()
        stdout = capture_stdout(capsys)
        
        assert stdout[-1] == expected_stdout
    
    def test_score_scores_individual_cards_in_a_hand(self):
        assert program.score(['two']) == 2
        assert program.score(['three']) == 3
        assert program.score(['four']) == 4
        assert program.score(['five']) == 5
        assert program.score(['six']) == 6
        assert program.score(['seven']) == 7
        assert program.score(['eight']) == 8
        assert program.score(['nine']) == 9
        assert program.score(['ten']) == 10
        assert program.score(['jack']) == 10
        assert program.score(['queen']) == 10
        assert program.score(['king']) == 10
        assert program.score(['ace']) == 11
    
    def test_score_scores_two_jack_and_ace_as_23(self):
        assert program.score(['two', 'jack', 'ace']) == 23

    @patch.object(random, 'randint', side_effect=[5, 10])
    @patch(f'{path}.input', side_effect=['hit', 'hit', 'stick'])
    def test_shows_score_so_far_when_game_is_played(self, mock_randint, mock_input, capsys):
        expected_stdout = [
            "Hit or stick? (NOT TESTED)",
            "hit (NOT TESTED)",
            "Score so far: 7",
            "Hit or stick? (NOT TESTED)",
            "hit (NOT TESTED)",           
            "Score so far: 17",
            "Hit or stick? (NOT TESTED)",
            "stick (NOT TESTED)",
            "You scored: 17"
            ]
 
        program.run_game()
        stdout = capture_stdout(capsys)

        assert expected_stdout[-7] in "".join(stdout)
        assert expected_stdout[-4] in "".join(stdout)
        assert expected_stdout[-1] in "".join(stdout)
    
    @patch.object(random, 'randint', side_effect=[6, 7, 12])
    @patch(f'{path}.input', side_effect=['hit', 'hit', 'hit', 'stick'])
    def test_player_takes_too_many_cards_and_busts(self, mock_randint, mock_input, capsys):
        expected_stdout = [
            "Hit or stick? (NOT TESTED)",
            "hit (NOT TESTED)",
            "Score so far: 8",
            "Hit or stick? (NOT TESTED)",
            "hit (NOT TESTED)",           
            "Score so far: 17",
            "Hit or stick? (NOT TESTED)",
            "hit (NOT TESTED)",
            "Score so far: 28",
            "Hit or stick? (NOT TESTED)",
            "stick (NOT TESTED)",
            "You busted with: 28"
            ]
        
        program.run_game()
        stdout = capture_stdout(capsys)

        assert expected_stdout[-10] in "".join(stdout)
        assert expected_stdout[-7] in "".join(stdout)
        assert expected_stdout[-4] in "".join(stdout)
        assert expected_stdout[-1] in "".join(stdout)


def capture_stdout(capsys):
    """Capture the preceding stdout and stderr and convert the stdout to a list,
    with every item corresponding to a line of stdout.
    """
    # capsys.readouterr() captures everything that is already in stdout and 
    # stderr.
    stdout, stderr = capsys.readouterr()

    # We then remove whitespace at the beginning and end, and split it into a 
    # list, with each line representing a line of stdout.
    return(stdout.strip().split('\n'))

