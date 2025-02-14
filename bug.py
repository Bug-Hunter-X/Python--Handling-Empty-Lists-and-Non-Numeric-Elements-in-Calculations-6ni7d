def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #this will return 0

my_list_with_zero = [1,0,3,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of a list with zero is: {average_zero}") #this will return 2.6

my_list_with_strings = [1,2,'a',4,5]
average_strings = calculate_average(my_list_with_strings) 
print(f"The average of a list with strings is: {average_strings}") #this will raise TypeError