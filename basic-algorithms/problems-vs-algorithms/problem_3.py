"""
Problem 3: Rearrange Array Elements

Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements are 
in the range [0, 9]. The number of digits in both the numbers cannot differ by 
more than 1. You're not allowed to use any sorting function that Python 
provides and the expected time complexity is O(nlog(n)).

You should implement the function body according to the rearrange_digits 
function signature. Use the test cases provided below to verify that your 
algorithm is correct. If necessary, add additional test cases to verify that 
your algorithm works correctly.
"""
def merge_sort_desc(arr: list[int]) -> list[int]:
    # Base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_desc(arr[:mid])
    right = merge_sort_desc(arr[mid:])

    return merge_desc(left, right)

def merge_desc(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    # Merge in descending order
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def rearrange_digits(input_list: list[int]) -> tuple[int, int]:
    if not input_list:
        return (0, 0)

    # Filter invalid values (just in case)
    input_list = [d for d in input_list if 0 <= d <= 9]
    if not input_list:
        return (0, 0)

    sorted_digits = merge_sort_desc(input_list)

    num1 = []
    num2 = []

    for digit in sorted_digits:
        if len(num1) <= len(num2):
            num1.append(str(digit))
        else:
            num2.append(str(digit))

    return int(''.join(num1)) if num1 else 0, int(''.join(num2)) if num2 else 0

def test_function(test_case: tuple[list[int], list[int]]) -> None:
    """
    Test the rearrange_digits function with a given test case.

    Args:
    test_case (tuple[list[int], list[int]]): A tuple containing two elements:
        - A list of integers representing the input array to be rearranged.
        - A list of two integers representing the expected output.

    Returns:
    None: Prints "Pass" if the sum of the output from rearrange_digits matches 
    the sum of the expected output, otherwise prints "Fail".
    """
    output: tuple[int, int] = rearrange_digits(test_case[0])
    solution: list[int] = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

if __name__ == '__main__':
    # Edge case: Single element list
    test_function(([9], [9, 0]))
    # Expected output: Pass

    # Normal case: Mixed positive and negative numbers
    test_function(([3, -2, 1, -4, 5], [53, 1]))    # Expected output: Pass

    # Normal case: list with zeros
    test_function(([0, 0, 0, 0, 0], [0, 0]))
    # Expected output: Pass

    # Normal case: list with repeated numbers
    test_function(([2, 2, 2, 2, 2], [222, 22]))
    # Expected output: Pass
