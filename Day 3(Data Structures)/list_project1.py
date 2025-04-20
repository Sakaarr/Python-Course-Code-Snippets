# Reverse a list without using .reverse() or [::-1] slicing.


def reverse(my_list):
    start = 0
    end = len(my_list) - 1
    while start <= end:
        my_list[start], my_list[end] = my_list[end], my_list[start]
        start += 1
        end -= 1
    return my_list

print(reverse([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

