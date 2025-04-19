#THIS IS THE BASIC SYNTAX OF PYTHON FUNCTIONS

def basic():
    print("Hello This is my first function")
    
basic()


# def = define a function
# basic = function name
# () = parentheses for optional inputs
# print() = what the function does
# basic() = Calling a Function

#FUNCTIONS WITH PARAMETERS

def para(name):
    print(f"Hello {name}, this is your first function with parameters")
    
para("SAKAR")

#FUNCTIONS WITH MULTIPLE PARAMETERS AND RETURN VALUES

def add(a, b):
    return a + b

sum = add(10,22.5)
print(f"The sum of 10 and 22.5 is {sum}")

# return sends back the result


#MULTIPLE RETURN VALUES

def summ(a,b):
    return a+b, a-b, a*b, a/b

a,b,c,d = summ(10,5)
print(f"The sum is {a}, the difference is {b}, the product is {c} and the division is {d}")