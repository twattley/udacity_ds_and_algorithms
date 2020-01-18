import unittest

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    if not isinstance(input_list, list):
        raise TypeError('input to rotated array search must be list')
        
    if not type(number) == int:
        raise TypeError('number to be searched must be int')
        
    start = 0
    end = len(input_list) - 1 #zero index means last = -1
    
    while start <= end:
        middle_index = start + (end - start) // 2
        
        if input_list[middle_index] == number: #while loop exit case 
            return middle_index
        
        if input_list[middle_index] >= input_list[start]:

            if input_list[start] <= number < input_list[middle_index]:
                end = middle_index - 1
            else: start = middle_index + 1
                
        else:
            if input_list[end] >= number > input_list[middle_index]: 
                start = middle_index + 1
            else: end = middle_index - 1
                
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

INPUT_LIST_1, EXPECTED_OUTPUT_1 = ([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
INPUT_LIST_2, EXPECTED_OUTPUT_2 = ([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
INPUT_LIST_3, EXPECTED_OUTPUT_3 = ([[6, 7, 8, 1, 2, 3, 4], 8])
INPUT_LIST_4, EXPECTED_OUTPUT_4 = ([[6, 7, 8, 1, 2, 3, 4], 1])
INPUT_LIST_5, EXPECTED_OUTPUT_5 = ([[6, 7, 8, 1, 2, 3, 4], 10])


class TestStringMethods(unittest.TestCase):
    
    """ test cases for huffman encoder """

    def test_input_error_1(self):
        with self.assertRaises(TypeError):
            rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4],'some_string')
    
    def test_input_error_2(self):
        with self.assertRaises(TypeError):
            rotated_array_search('some_string', 5)
    
    def test_rotated_array_search(self):
        assert linear_search(
                    INPUT_LIST_1, EXPECTED_OUTPUT_1) == rotated_array_search(
                                                            INPUT_LIST_1, EXPECTED_OUTPUT_1)
        assert linear_search(
                    INPUT_LIST_2, EXPECTED_OUTPUT_2) == rotated_array_search(
                                                            INPUT_LIST_2, EXPECTED_OUTPUT_2)
        assert linear_search(
                    INPUT_LIST_3, EXPECTED_OUTPUT_3) == rotated_array_search(
                                                            INPUT_LIST_3, EXPECTED_OUTPUT_3)
        assert linear_search(
                    INPUT_LIST_4, EXPECTED_OUTPUT_4) == rotated_array_search(
                                                            INPUT_LIST_4, EXPECTED_OUTPUT_4)
        assert linear_search(
                    INPUT_LIST_5, EXPECTED_OUTPUT_5) == rotated_array_search(
                                                            INPUT_LIST_5, EXPECTED_OUTPUT_5)
        
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)