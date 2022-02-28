import subprocess

class TestQuestion2():
    def test_sums_1_to_250_and_prints_result(self):
        expected_stdout = '31375'
        
        stdout = subprocess.check_output(["python3",
            "chapter4/questions/question_2.py"]).decode().strip()
        
        assert stdout == expected_stdout