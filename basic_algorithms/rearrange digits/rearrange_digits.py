import unittest

def reverse_mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = reverse_mergesort(left)
    right = reverse_mergesort(right)
    
    return reverse_merge(left, right)
    
def reverse_merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    
    if not isinstance(input_list, list):
        raise TypeError('input to rearrange digits must be a list')

    if not len(input_list) >= 2:
        raise AttributeError('list must be greater than 2 to split and re-arrange')
        
    sorted_list = reverse_mergesort(input_list)
    
    first_num = int(''.join(str(v) for i,v in enumerate(sorted_list) if not i%2)) 
    second_num = int(''.join(str(v) for i,v in enumerate(sorted_list) if i%2))
    
    return [first_num, second_num]
    

INPUT_LIST_1, EXPECTED_OUTPUT_1 = ([[1, 2, 3, 4, 5], [531, 42]])
INPUT_LIST_2, EXPECTED_OUTPUT_2 = ([[4, 6, 2, 5, 9, 8], [964, 852]])

class TestStringMethods(unittest.TestCase):
    
    """ test cases for huffman encoder """

    def test_input_error_1(self):
        with self.assertRaises(TypeError):
            rearrange_digits(1)
            
    def test_input_error_3(self):
        with self.assertRaises(AttributeError):
            rearrange_digits([2])
    
    def test_rearrange_digits(self):
        assert rearrange_digits(INPUT_LIST_1) == EXPECTED_OUTPUT_1
        assert rearrange_digits(INPUT_LIST_2) == EXPECTED_OUTPUT_2
    
#run tests
unittest.main(argv=['first-arg-is-ignored'], exit=False)