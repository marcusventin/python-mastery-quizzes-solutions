import subprocess

class TestQuestion1():
    def test_prints_nums_1_to_20_except_Fizz_if_divisible_by_3_Buzz_if_divisible_by_5_and_FizzBuzz_if_divisible_by_20(self):   
        # We join the list of items with \n, meaning that each list item will be
        # presented on a new line.
        expected_stdout = '\n'.join([
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
            "16",
            "17",
            "Fizz",
            "19",
            "Buzz"
            ])

        stdout = subprocess.check_output(["python3",
            "chapter4/questions/question_1.py"]).decode().strip()

        assert stdout == expected_stdout