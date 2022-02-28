import subprocess

class TestQuestion1():
    def test_outputs_number(self):
        # The subprocess module enables you to run external programs. The list 
        # argument is turned into a terminal command, with each entry separated 
        # by a space. In this case, we are running 
        # 'python3 chapter1/questions/question_1.py'. The .check_output() 
        # function captures the stdout from this action, and saves it to the 
        # stdout variable.
        stdout = subprocess.check_output(["python3",
            "chapter1/questions/question_1.py"])

        # The terminal output is saved in the bytes format, so we use the 
        # .decode() function to convert it to a string, which we save to the
        # decoded_stdout variable.
        decoded_stdout = stdout.decode()

        # We now want to check that this string can be converted to an integer. 
        # The int() function performs this role. We use the assert statement to
        # test whether this function can be performed without raising an error.
        # If so, the test passes.
        assert int(decoded_stdout)

        # This test cannot actually determine whether an integer-type object has
        # been printed, only that an object which can be converted to an integer
        # has been printed.

