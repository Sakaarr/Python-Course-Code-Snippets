#BASICS OF LIST
numbers = [10, 20, 30, 40, 50]
print(numbers[0])     # 10
print(numbers[-1])    # 50 (last element)
print(numbers[1:4])   # [20, 30, 40]
print(numbers[1:])    # [20, 30, 40, 50] (from index 1 to end)
print(numbers[:3])    # [10, 20, 30] (from start to index 2)
print(numbers[::2])   # [10, 30, 50] (every second element)
print(numbers[::-1])  # [50, 40, 30, 20, 10] (reversed list)

#MODIFYING LISTS

numbers[1] = 25  # Change the second element to 25
print(numbers)  # [10, 25, 30, 40, 50]
numbers.append(60)  # Add 60 to the end of the list
print(numbers)  # [10, 25, 30, 40, 50, 60]
numbers.insert(2, 35)  # Insert 35 at index 2
print(numbers)  # [10, 25, 35, 30, 40, 50, 60]
numbers.remove(25)  # Remove the first occurrence of 25
popped = numbers.pop()  # Remove and return the last element (60)
print(popped)  # 60
print(numbers)  # [10, 25, 35, 30, 40, 50]


#LOOPING THROUGH A LIST

for num in numbers:
    print(num)  # Prints each number in the list
    
for i in range(len(numbers)):
    print(i,numbers[i])  # Prints each number using its index
    
    
#NESTING LISTS
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][2]) # 3 (first row, third column)
print(matrix[1][2]) # 6 (second row, third column)