#Take input from user tell them their age and other parameters also do manipulation on it using all the things we learned in day 1

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

if age>=18:
    print("You are an adult")
else:
    print("You are a minor")

if height>=5.5:
    print("You are tall enough to ride the roller coaster")
else:
    print("You are not tall enough to ride the roller coaster. Grow Up Drink Complan")

print("\n")
print("You will be", age+10, "years old in 10 years.")

for i in range(1, int(age)+1):
    print("You were", i, "years old", age-i, "years ago.")
    print("\n")
print("Your name is", name, "and your height is", height, "feet.")