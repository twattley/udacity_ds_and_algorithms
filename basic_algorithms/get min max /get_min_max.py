import unittest
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    
    if len(ints) ==1:
        raise ValueError('min max must be called with at least 2 arguments')
    
    if not ints:
        raise AttributeError('get_min_max function must be called with value')
    
    if not isinstance(ints, list):
        raise TypeError('input must be a list')
    
    if not type(ints[0]) == int:
        raise TypeError('there are some non integer values in the list')
    
    min_num = ints[0]
    max_num = ints[0]
    
    for i in ints:
        if not type(i) == int:
            raise TypeError('Unable to compare strings to ints')
        if i > max_num:
            max_num = i
        if i < min_num:
            min_num = i

    return min_num, max_num




TEST_LIST_1 = [random.randrange(0, 100, 1) for i in range(20)]
TEST_LIST_2 = [random.randrange(0, 100, 1) for i in range(20)]
TEST_LIST_3 = [random.randrange(0, 100, 1) for i in range(20)]


class TestMinMax(unittest.TestCase):
    
    """ test cases for min max function """
    
    def test_value_error(self):
        with self.assertRaises(ValueError):
            get_min_max([5])

    def test_list_error(self):
        with self.assertRaises(TypeError):
            get_min_max('some string input')
    
    def test_int_error(self):
        with self.assertRaises(TypeError):
            get_min_max([1,'some string input',2])
    
    def test_get_min_max_function(self):
        min_num, max_num = get_min_max(TEST_LIST_1)
        assert min_num == min(TEST_LIST_1)
        assert max_num == max(TEST_LIST_1)
        min_num, max_num = get_min_max(TEST_LIST_2)
        assert min_num == min(TEST_LIST_2)
        assert max_num == max(TEST_LIST_2)
        min_num, max_num = get_min_max(TEST_LIST_3)
        assert min_num == min(TEST_LIST_3)
        assert max_num == max(TEST_LIST_3)
        
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)
    