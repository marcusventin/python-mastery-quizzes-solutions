import subprocess

class TestQuestion3():
    def test_prints_first_20_Fibonacci_numbers(self):
        expected_stdout = '\n'.join([
            "0",
            "1",
            "1",
            "2",
            "3",
            "5",
            "8",
            "13",
            "21",
            "34",
            "55",
            "89",
            "144",
            "233",
            "377",
            "610",
            "987",
            "1597",
            "2584",
            "4181"])
        
        stdout = subprocess.check_output(["python3",
            "chapter4/questions/question_3.py"]).decode().strip()

        assert stdout == expected_stdout