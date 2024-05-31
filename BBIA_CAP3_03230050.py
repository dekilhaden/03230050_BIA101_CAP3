# https://github.com/dekilhaden/03230050_BIA101_CAP3.git
# Deki Lhadon
# BBIA
# 03230050
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.w3schools.com/python/python_files.asp
# https://www.tutorialspoint.com/python/python_files_io.htm
################################
# SOLUTION
# Your Solution Score: <242740>

# Read the input.txt file 
def read_input(file_path): # It defines a function named read_input that takes a file_path as input.
    lines = [] # This line creates an empty list called lines to store the lines from the file.
    with open(file_path, 'r') as file: # This line opens the file located at file_path in read mode ('r') and assigns it to the variable file.
        for line in file: # This line starts a loop that iterates over each line in the file.
            line = line.strip() # This line removes any leading or trailing whitespace characters from the line.
            if line: # This line checks if the line is not empty after removing the whitespace characters.
                lines.append(line) # If the line is not empty, this line adds it to the lines list.
    return lines # This line returns the lines list containing all non-empty lines from the file.

def calculate_sum(lines): # This line defines a function named calculate_sum that takes a list of lines as input.
    total_sum = 0 # This line initializes a variable total_sum to zero, which will store the sum of two-digit numbers extracted from the lines.
    for line in lines: # This line starts a loop that iterates over each line in the lines list.
        first_digit = int(line[0]) if line[0].isdigit() else 0 # This line extracts the first character from the line and converts it to an integer if it's a digit, otherwise, it assigns 0 to first_digit.
        last_digit = int(line[-1]) if line[-1].isdigit() else 0 # This line extracts the last character from the line and converts it to an integer if it's a digit, otherwise, it assigns 0 to last_digit.
        two_digit_number = first_digit * 10 + last_digit # This line combines the first_digit and last_digit to form a two-digit number.
        total_sum += two_digit_number # This line adds the two_digit_number to the total_sum.
    return total_sum # This line adds the two_digit_number to the total_sum.

def print_solution(file_path, total_sum): # This line defines a function named print_solution that takes a file_path and total_sum as input.
 print(f"The total sum from the given input file {file_path} is {total_sum}") # This line prints a formatted string that includes the file_path and total_sum.

# Main code
file_path = '03230050_BIA101_CAP3\\050.txt'  # This line assigns the file path to the variable file_path.
lines = read_input(file_path) # This line calls the read_input function with the file_path and stores the returned lines in the lines variable.
total_sum = calculate_sum(lines) # This line calls the calculate_sum function with the lines and stores the returned sum in the total_sum variable.
print_solution(file_path, total_sum) # This line calls the print_solution function with the file_path and total_sum to print the solution.