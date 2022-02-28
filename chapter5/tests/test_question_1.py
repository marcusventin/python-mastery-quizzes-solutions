import subprocess

class TestQuestion1():
    def test_always_prints_one_of_the_magic_8_ball_responses(self):
        responses = ["It is certain",
                    "It is decidedly so",
                    "Ask again later",
                    "Outlook not so good",
                    "Very doubtful"]
        
        # We run the Question 1 program and save its stdout as an item in the 
        # stdout list 20 times. (This method of generating a list is called list 
        # comprehension)
        stdout = [run_question_1() for x in range(20)]

        # We look at every response in our stdout list, and check that it is 
        # found in our list of approved responses.
        for response in stdout:
            assert response in responses

def run_question_1():
    """Run the Question 1 program, returning the stdout as a string stripped
    of whitespace.
    """
    return(subprocess.check_output(["python3",
            "chapter5/questions/question_1.py"]).decode().strip())

        