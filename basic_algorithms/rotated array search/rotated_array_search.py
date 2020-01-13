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

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

