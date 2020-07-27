
#
def odd_even_counter(number):
    odd_even_list = [0, 0]  # create list (not blank)
    # for loop with range (start number, stop number, step)
    for i in range(number,0,-1):  # Iterate over number, decrementing by 1 until 0 is reached
        if i % 2 == 0:  # if the number is even
            odd_even_list[0] = odd_even_list[0] + i  # add the number to this list
        else:  # id the number is odd
            odd_even_list[1] = odd_even_list[1] + i  # add the number to this list
    return odd_even_list

print(odd_even_counter(5))  # [6, 9]

