#Simple code for calculator (Comment all other coders from line 23 to below to run this)
# no = int(input("Enter the number of numbers you want to perform on: "))
# if no == 0:
#     print("No Operation Can Be Performed")
# else:
#     result = int(input("Enter number 1: "))  # Start with the first number
#     for i in range(1, no):
#         num = int(input(f"Enter number {i+1}: "))
#         operation = input("Enter the operation you want to perform (+, -, *, /): ")
#         if operation == "+":
#             result += num
#         elif operation == "-":
#             result -= num
#         elif operation == "*":
#             result *= num
#         elif operation == "/":
#             if num != 0:
#                 result /= num
#             else:
#                 print("Cannot divide by zero")
#     print(f"The result is: {result}")

#Optimized code using functions(Comment codes from 1 to 22 and 75 to 121 to run this)

# def perform_operation(result, num, operation):
#     if operation == "+":
#         return result + num
#     elif operation == "-":
#         return result - num
#     elif operation == "*":
#         return result * num
#     elif operation == "/":
#         if num == 0:
#             print("Cannot divide by zero. Skipping this operation.")
#             return result
#         return result / num
#     else:
#         print("Invalid operation. Skipping this operation.")
#         return result

# def main():
#     try:
#         count = int(input("Enter the number of numbers you want to perform on: "))
#     except ValueError:
#         print("Invalid input. Please enter an integer.")
#         return

#     if count <= 0:
#         print("No operation can be performed.")
#         return

#     try:
#         result = float(input("Enter number 1: "))  # Use float for division accuracy
#     except ValueError:
#         print("Invalid number.")
#         return

#     for i in range(1, count):
#         try:
#             num = float(input(f"Enter number {i+1}: "))
#         except ValueError:
#             print("Invalid number. Skipping...")
#             continue

#         operation = input("Enter the operation (+, -, *, /): ").strip()
#         result = perform_operation(result, num, operation)

#     print(f"The final result is: {result}")

# if __name__ == "__main__":
#     main()

#Let User Enter all the numbers and operations at once

def perform_operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            print("Cannot divide by zero. Skipping operation.")
            return a
        return a / b
    else:
        print(f"Invalid operation '{op}'. Skipping.")
        return a

def main():
    expression = input("Enter expression (e.g., 5 + 3 * 2 / 4): ").strip()
    tokens = expression.split()

    if len(tokens) < 3 or len(tokens) % 2 == 0:
        print("Invalid expression format. Please enter in the format: number op number op number...")
        return

    try:
        result = float(tokens[0])
    except ValueError:
        print(f"Invalid number: {tokens[0]}")
        return

    i = 1
    while i < len(tokens) - 1:
        op = tokens[i]
        try:
            num = float(tokens[i + 1])
        except ValueError:
            print(f"Invalid number: {tokens[i + 1]}. Skipping.")
            i += 2
            continue

        result = perform_operation(result, num, op)
        i += 2

    print(f"The final result is: {result}")

if __name__ == "__main__":
    main()
