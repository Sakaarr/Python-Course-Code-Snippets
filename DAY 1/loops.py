#FOR LOOP

#PRINT THE TEXTS FOR FEW TIMES
i=0
for i in range(5):
    print("Hello World")
    
# WHILE LOOPS

while i < 5:
    print("Hello World")
    i += 1


#PRINT NUMBERS FROM 1 TO 10

for i in range(10):
    print(i+1)
    print("\n")    

# PRINT MULTIPLICATION OF ANY NUMBER
num = int(input("Enter a number: "))
range_num = int(input("Enter the range: "))
for i in range(range_num+1):
    print(num*i)
    print("\n")