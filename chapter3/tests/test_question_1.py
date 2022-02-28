import chapter3.questions.question_1 as program

class TestQuestion1():
    def test_defines_five_by_filling_in_the_blank(self):
        assert program.five == 5

    def test_defines_seven_by_filling_in_the_blank(self):
        assert program.seven == 7
    
    def test_defines_two_by_filling_in_the_blank(self):
        assert program.two == 2

    def test_defines_three_point_zero_by_filling_in_the_blank(self):
        assert program.three_point_zero == 3.0
    
    def test_defines_two_is_integer_by_filling_in_the_blank(self):
        assert program.two_is_integer == True
    
    def test_defines_four_by_filling_in_the_blank(self):
        assert program.four == 4
    
    def test_defines_zero_by_filling_in_the_blank(self):
        assert program.zero == 0


