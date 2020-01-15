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
        
    sorted_list = mergesort(input_list)
    
    first_num = int(''.join(str(v) for i,v in enumerate(sorted_list) if not i%2)) 
    second_num = int(''.join(str(v) for i,v in enumerate(sorted_list) if i%2))
    
    return [first_num, second_num]
    
    

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]