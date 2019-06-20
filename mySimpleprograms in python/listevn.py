def _list_of_even_numbers_sample_(a, b):
    output_list = []
    for number in range(a, b):
        # check if the number is even
        if number % 2 == 0:
            # if true put the numbers in the output list
            output_list.append(number)
    return output_list
def _list_of_odd_numbers_sample_(a, b):
    output_list = []
    for number in range(a, b):
        # check if the number is even
        if number % 2 != 0:
            # if true put the numbers in the output list
            output_list.append(number)
    return output_list
print(_list_of_odd_numbers_sample_(30,80))