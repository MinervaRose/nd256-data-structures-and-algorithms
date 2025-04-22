"""
Problem 1: Square Root of an Integer

In this problem, you need to find the square root of a given integer without using 
any Python libraries. You should return the floor value of the square root.

Below is a function signature that serves as a starting point for your implementation. 
Your task is to complete the body of the function. Additionally, some test cases are 
provided to help you verify the correctness of your implementation. If necessary, add 
test cases to verify that your algorithm is working properly.

The expected time complexity is O(log(n)).
"""

def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number using binary search.

    Args:
    number (int): Number to find the floored square root of

    Returns:
    int: Floored square root of the number
    """
    if number < 0:
        return -1  # Handle negative input safely
    if number == 0 or number == 1:
        return number

    start = 0
    end = number
    result = 0

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


if __name__ == "__main__":
    # Standard test cases
    print("Pass" if 3 == sqrt(9) else "Fail")
    print("Pass" if 0 == sqrt(0) else "Fail")
    print("Pass" if 4 == sqrt(16) else "Fail")
    print("Pass" if 1 == sqrt(1) else "Fail")
    print("Pass" if 5 == sqrt(27) else "Fail")

    # Edge test case: Large number
    print("Pass" if 31622 == sqrt(1000000000) else "Fail")  # sqrt(1e9) ≈ 31622.7

    # Edge test case: Negative number
    print("Pass" if -1 == sqrt(-25) else "Fail")  # Negative input handled
