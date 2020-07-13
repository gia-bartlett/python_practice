# A little one I added after the 2nd exercise
import time


def prime_number(number):
    #number = int(input("Please enter a number between 1-100:  "))  # input for number between 1-100
    distinct = 0  # starting with a variable set to zero
    divisors = []  # creating an empty list to populate with divisors
    for i in range(2, number, 1):  # creating a list starting at 2, ending one before number and incrementing by 1
        # print(f"testing {i}")
        if number % i == 0:
            #print(f"The number {number} is not a prime because it can be divided by {i}")
            distinct += 1  # add 1 to distinct to count how many times the number was divisible by a number
            divisors.append(i)  # add the dividing number to this list
        #time.sleep(0.1)  # slows down the program to help visualise
    if distinct == 0:
        print(f"The number {number} is prime!")
    else:
        print(f"The number {number} is not prime because it can be divided {distinct} times by {divisors}.")


def prime_number_tester():
    print("Starting...")  # welcome message
    time.sleep(1)
    exit = True  # setting the variable exit
    while exit:  # while exit is True this will keep running...for ever.
        choice = int(input("Please choose a number or choose 0 to exit: "))
        #print(type(choice))
        if choice == 0:
            print("kthnxbye")
            exit = False
        # elif type(choice) != int:
        #     print("Please choose a number!")
        elif choice <0:
            print("Please choose a positive number")
        else:
            prime_number(choice)


prime_number_tester()