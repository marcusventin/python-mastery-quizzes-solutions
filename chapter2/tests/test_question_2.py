import subprocess

import chapter2.questions.question_2 as program

class TestQuestion2(): 
    def test_TWELVE_equals_12(self):
        assert program.TWELVE == 12
    
    def test_FOURTEEN_equals_14(self):
        assert program.FOURTEEN == 14
    
    def test_SIXTEEN_equals_16(self):
        assert program.SIXTEEN == 16

    def test_prints_2688(self):
        expected_stdout = '2688'
        
        # We can make our code more concise by putting the commands that run our
        # file, capture its output, and convert it to a string on one line. We 
        # also add the .strip() function, which removes whitespace from the 
        # stdout.
        stdout = subprocess.check_output(["python3",
            "chapter2/questions/question_2.py"]).decode().strip()

        assert stdout == expected_stdout

    