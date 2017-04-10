def seconds(number_list):
    for i in number_list:
        return number_list[1::2]
    # Create a function that takes a list as a parameter,
    # and returns a new list with every second element from the orignal list
    # example: [1, 2, 3, 4, 5] should produce [2, 4]

print(seconds([1, 2, 3, 4, 5])) # should print [2, 4]
