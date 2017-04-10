    # Create a function that takes a filename as string parameter,
    # counts the occurances of the letter "a", and returns it as a number.
    # If the file does not exist, the function should return 0 and not break.

file = open("afile.txt" , "r")
text = file.read()
file.close

def count_as(filename):
    try:
        text = open(filename, 'r')
        number_of_as = 0
        for letter in text:
            if letter =='a' or letter == 'A':
                number_of_as += 1
        return number_of_as
    except FileNotFoundError:
        print('0')


print(count_as("afile.txt")) # should print 28
print(count_as("not-a-file")) # should print 0
