# Create a function is_even(num) that returns True if number is even

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

a=is_even(4) # True
b=is_even(5) # False

print(a,b)


# Create a function greet_user(name) that prints a greeting.

def greet_user(name):
    print(f"Hello, {name}! Welcome to the program.")
    
    
greet_user("Sakar")

# Create a calculator function that takes 2 numbers and an operator.

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"
    
a = calculator(10,5,"+")
b = calculator(10,5,"-")
c = calculator(10,5,"*")
d = calculator(10,5,"/")
print(a,b,c,d)

# Write a function that takes a list of numbers and returns the sum.

def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

a = sum_of_list([1, 2, 3, 4, 5])

print(a) # 15

# Write a function to find the maximum of 3 numbers.

def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

max = max_of_three(10, 20, 30)
print(max) # 30