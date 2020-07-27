
number = int(input("Please enter a number:  "))  # input for number

if number % 2 == 0:  # if the number divided by 2 has no remainder
    print(f"The number {number} is even!")  # then it is even
else:
    print(f"The number {number} is odd!")  # otherwise, it is odd

''' SOLUTION:
num = input("Enter a number: ")
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")'''