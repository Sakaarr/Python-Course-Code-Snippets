# Find the Second Largest Number in a List

def second_largest(numbers):
    if len(numbers) < 2:
        return None
    largest = second = float('-inf')
    for num in numbers:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num
    return second if second != float('-inf') else None

print(second_largest([10, 20, 4, 45, 99]))  # Output: 45
            