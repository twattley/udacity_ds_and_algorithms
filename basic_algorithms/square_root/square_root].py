import math
import unittest

def squareroot(number):
    
    if not type(number) == int:
        raise TypeError('input must be an integer')
       
    #0 case
    if number == 0:
        return 0
   
    if not number > 0:
        raise ValueError('intger must be positive')
    
    #return 1 for anything 3 and under
    if number <= 3:
        return 1

    start = 1
    end = number

    while start <= end:
        middle = (start + end) // 2

        if middle**2 == number:
            square_root = middle
            return square_root #while loop exit case

        if middle**2 < number:
            start = middle + 1
            square_root = middle
        else:
            end = middle - 1
            
    return square_root


def test_helper_function(number):
   
    """ helper using builtins to test square root function """
   
    return math.floor(math.sqrt(number))

class TestSquareRoot(unittest.TestCase):
   
    """ test cases for square root function """
   

    def test_type_error(self):
        with self.assertRaises(TypeError):
            squareroot('some string')
   
    def test_value_error(self):
        with self.assertRaises(ValueError):
            squareroot(-4)
   
    def test_square_root_function(self):
   
        assert squareroot(9) == test_helper_function(9)
        assert squareroot(903420) == test_helper_function(903420)
        assert squareroot(45) == test_helper_function(45)
        assert squareroot(22) == test_helper_function(22)
        assert squareroot(1) == test_helper_function(1)
        assert squareroot(3) == test_helper_function(3)
        assert squareroot(2) == test_helper_function(2)
   


#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)

    