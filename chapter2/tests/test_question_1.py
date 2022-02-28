import chapter2.questions.question_1 as program
# By importing Question 1 and defining it as program, we can access its 
# variables using program.VAR_NAME.

class TestQuestion2():
    def test_ONE_equals_1(self):
        # Here, we check that the ONE variable in the Question 1 file is equal 
        # to 1.
        assert program.ONE == 1
    
    def test_TWO_equals_2(self):
        assert program.TWO == 2
    
    def test_THREE_equals_3(self):
        assert program.THREE == 3
    
    def test_FOUR_equals_4(self):
        assert program.FOUR == 4
    
    def test_FIVE_equals_5(self):
        assert program.FIVE == 5
    
    def test_SIX_equals_6(self):
        assert program.SIX == 6
    
    def test_SEVEN_equals_7(self):
        assert program.SEVEN == 7
    
    def test_EIGHT_equals_8(self):
        assert program.EIGHT == 8
    
    def test_NINE_equals_9(self):
        assert program.NINE == 9
    
    def test_TEN_equals_10(self):
        assert program.TEN == 10