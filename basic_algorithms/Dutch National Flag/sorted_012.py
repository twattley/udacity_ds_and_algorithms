import random
import unittest

#generate some dummy test data
LIST_A = [random.randrange(0, 3, 1) for i in range(20)]
LIST_B = [random.randrange(0, 3, 1) for i in range(20)]
LIST_C = [random.randrange(0, 3, 1) for i in range(20)]


def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zeros = []
    ones = []
    twos = []
    
    if not input_list:
        raise ValueError('no list input!!')
    
    for i in input_list:
        
        if not isinstance (i, int):
            raise TypeError('Input to sort_012 function must be an integer')
        
        if i == 0:
            zeros.append(i)
        elif i == 1:
            ones.append(i)
        elif i == 2:
            twos.append(i)
        else:
            raise ValueError('Input to sort_012 function must be between 1 and 2')
            
    return zeros + ones + twos
        


class TestSort012(unittest.TestCase):
    
    """ test sort 012 function """

    def test_type_error(self):
        with self.assertRaises(TypeError):
            sort_012([1, 2, 0, 2, 1, 0, 0, 2, 'string', 1, 2, 0, 0, 2, 2, 1, 1, 1, 2, 2])
    
    def test_value_error(self):
        with self.assertRaises(ValueError):
            sort_012([1, 2, 0, 2, 1, 0, 0, 2, 0, 1, 3, 0, 0, 2, 2, 1, 1, 1, 2, 2])
            
    def test_no_input_error(self):
        with self.assertRaises(ValueError):
            sort_012('')
            
    def test_correct_input(self):
        assert sort_012(list_a) == sorted(list_a)
        assert sort_012(list_b) == sorted(list_b)
        assert sort_012(list_c) == sorted(list_c)
    
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)