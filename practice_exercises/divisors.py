number = int(input("Please enter a number: "))

def divide_by(number):
    divisors = []  # creating an empty list to populate
    for i in range(2, number, 1):  # create a list from 2-one before number entered
        #print(f"testing {i}")
        if number % i == 0:  # if there is no remainder then the number is divisible by that number
            divisors.append(i)  # add the divisor number to the list
    print(f"The number {number} can be divided by {divisors}")

divide_by(number)


''' SOLUTION:
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
'''